import { Component } from '@angular/core';
import { BaseComponent } from '../base/base.component';
import { CardColor, CardColors2DisplayStr, CardSymbol, CardSymbol2DisplayStr, GameStates, GameStates2DisplayStr } from 'src/app/util/const';
import { CardDTO, DeckDTO, PlayerDTO } from 'src/app/service/api/schema/get-game-info';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/service/api/api.service';
import { timer } from 'rxjs';

@Component({
  selector: 'app-wait',
  templateUrl: './wait.component.html',
  styleUrls: ['./wait.component.scss']
})
export class WaitComponent extends BaseComponent {

  game_id = -1
  game_states = GameStates.unknown
  player_id = -1
  host = -1
  player_list: PlayerDTO[] = []
  deck_list: DeckDTO[] = []

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private route: ActivatedRoute,
    private api: ApiService,
    private router: Router,
  ) {
    super()
  }

  ngOnInit(): void {
    let queryParamMap = this.route.snapshot.queryParamMap
    let game_id = queryParamMap.get('game_id')
    let player_id = queryParamMap.get('player_id')
    if (game_id && player_id) {
      this.game_id = parseInt(game_id)
      this.player_id = parseInt(player_id)

      this.autoUnsubscribeObserver(timer(0, 3000))
      .subscribe(() => {
        this.onRefreshGameClicked()
      })
    }
    else {
      this.router.navigate(['/'])
    }
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  getGameStatesDisplayStr() {
    return GameStates2DisplayStr[this.game_states]
  }

  getCardList(player_id: number) {
    let deck = this.deck_list.find(deck => deck.player_id == player_id)
    if (!deck) {
      return []
    }
    return deck.card_list
  }

  getCardDisplayStr(dto: CardDTO) {

    let result = ''
    if (dto) {
      let color: CardColor = dto.color
      result += CardColors2DisplayStr[color]
      let symbol: CardSymbol = dto.symbol
      result += CardSymbol2DisplayStr[symbol]
    }

    return result
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  async onRefreshGameClicked() {
    // console.log('onRefreshGameClicked')

    let result = await this.api.getGameInfo(this.game_id)
    if (!result.isSuccess) {
      return
    }
    this.game_states = result.body.game_states
    if (this.game_states === GameStates.preparing || this.game_states === GameStates.playing) {
      let queryParams = {
        game_id: this.game_id,
        player_id: this.player_id,
      }
      this.router.navigate(['/game'], { queryParams })
    }

    this.host = result.body.host
    this.player_list = result.body.player_list
    this.deck_list = result.body.deck_list
  }

  async onStartGameClicked() {

    let result = await this.api.startGame(this.game_id, this.player_id)
    if (!result.isSuccess) {
      alert(result.errorMsg)
      return
    }
    this.onRefreshGameClicked()
  }

  async onPlayCardClicked(player_id: number, index: number) {

    let result = await this.api.playCard(this.game_id, player_id, index)
    if (!result.isSuccess) {
      alert(result.errorMsg)
      return
    }
    this.onRefreshGameClicked()
  }
}
