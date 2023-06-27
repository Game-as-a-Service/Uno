import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/service/api/api.service';
import { DeckDTO, PlayerDTO } from 'src/app/service/api/schema/get-game-info';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {

  game_id = -1
  game_states = -1
  player_id = -1
  host = -1
  player_list: PlayerDTO[] = []
  deck_list: DeckDTO[] = []

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private route: ActivatedRoute,
    private api: ApiService,
    private router: Router,
  ) { }

  ngOnInit(): void {
    let queryParamMap = this.route.snapshot.queryParamMap
    let game_id = queryParamMap.get('game_id')
    let player_id = queryParamMap.get('player_id')
    if (game_id && player_id) {
      this.game_id = parseInt(game_id)
      this.player_id = parseInt(player_id)
      setInterval(() => {
        this.onRefreshGameClicked()
      }, 3000)
      this.onRefreshGameClicked()
    }
    else {
      this.router.navigate(['/'])
    }
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  getCardList(player_id: number) {
    let deck = this.deck_list.find(deck => deck.player_id == player_id)
    if (!deck) {
      return []
    }
    return deck.card_list
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  async onRefreshGameClicked() {

    let result = await this.api.getGameInfo(this.game_id)
    if (!result.isSuccess) {
      return
    }
    this.game_states = result.body.game_states
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

}
