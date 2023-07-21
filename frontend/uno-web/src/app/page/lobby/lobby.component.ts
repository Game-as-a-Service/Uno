import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/service/api/api.service';
import { BaseComponent } from '../base/base.component';
import { timer } from 'rxjs';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss']
})
export class LobbyComponent extends BaseComponent {

  player_id = -1
  game_id_list: number[] = []

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
    let player_id = queryParamMap.get('player_id')
    if (player_id) {
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

  async onCreateJoinClicked() {

    let result = await this.api.createGame()
    if (!result.isSuccess) {
      alert(result.errorMsg)
      return
    }

    console.log('result_create', result);

    let game_id = result.body.game_id
    if (!game_id) {
      return
    }

    this.onJoinGameClicked(game_id)
  }

  async onRefreshGameClicked() {

    let result = await this.api.getGameList()
    if (!result.isSuccess) {
      alert(result.errorMsg)
      return
    }
    this.game_id_list = result.body.game_id_list
  }

  async onJoinGameClicked(game_id: number) {

    let player_id = this.player_id
    let result = await this.api.joinGame(game_id, player_id)
    console.log('result', result);

    if (!result.isSuccess) {
      alert(result.errorMsg)
      return
    }

    let queryParams = {
      game_id,
      player_id,
    }
    this.router.navigate(['/wait'], { queryParams })
  }
}
