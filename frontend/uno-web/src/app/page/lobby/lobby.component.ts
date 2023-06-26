import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/service/api/api.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss']
})
export class LobbyComponent implements OnInit {

  player_id = -1

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private route: ActivatedRoute,
    private api: ApiService,
    private router: Router,
  ) { }

  ngOnInit(): void {
    let queryParamMap = this.route.snapshot.queryParamMap
    let player_id = queryParamMap.get('player_id')
    if (player_id) {
      this.player_id = parseInt(player_id)
    }
    else {
      this.router.navigate(['/'])
    }
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  async onCreateJoinClicked() {

    let result_create = await this.api.createGame()
    if (!result_create.isSuccess) {
      return
    }

    console.log('result_create', result_create);

    let game_id = result_create.body.game_id
    if (!game_id) {
      return
    }

    let player_id = this.player_id
    let result_join = await this.api.joinGame(game_id, player_id)
    console.log('result_join', result_join);

    if (!result_join.isSuccess) {
      return
    }

    let queryParams = {
      game_id,
      player_id,
    }
    this.router.navigate(['/game'], { queryParams })
  }
}
