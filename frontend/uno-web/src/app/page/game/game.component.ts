import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/service/api/api.service';
import { DeckDTO, PlayerDTO } from 'src/app/service/api/schema/get-game-info';
import { GameStates, GameStates2DisplayStr } from 'src/app/util/const';
import { BaseComponent } from '../base/base.component';
import { timer } from 'rxjs';
import { CardViewModel } from 'src/app/component/share/card.viewmodel';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent extends BaseComponent {

  game_id = -1
  game_states = GameStates.unknown
  player_id = -1
  player_list: PlayerDTO[] = []
  deck_list: DeckDTO[] = []

  // 整理過後
  cardViewDict: { [key: number]: CardViewModel } = {}

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

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  async onRefreshGameClicked() {
    // console.log('onRefreshGameClicked')

    let result = await this.api.getGameInfo(this.game_id)
    if (!result.isSuccess) {
      return
    }
    this.game_states = result.body.game_states

    this.player_list = result.body.player_list
    this.deck_list = result.body.deck_list

    // 需要找到自己的牌 排在第一個 然後順下去
    let playerIndex = this.player_list.findIndex(player => player.id == this.player_id)
    for (let i = 0; i < this.player_list.length; i++) {
      let index = (playerIndex + i) % this.player_list.length
      let player = this.player_list[index]
      let deck = this.deck_list.find(deck => deck.player_id == player.id)
      if (!deck) {
        continue
      }
      let cardView = new CardViewModel()
      cardView.player = player
      cardView.deck = deck
      this.cardViewDict[i] = cardView
    }
    // console.log(this.cardViewDict)
  }

  async onPlayCardClicked(index: number, player_index: number) {

    let player_id = this.cardViewDict[player_index].player?.id || -1
    let result = await this.api.playCard(this.game_id, player_id, index)
    if (!result.isSuccess) {
      alert(result.errorMsg)
      return
    }
    this.onRefreshGameClicked()
  }
}
