import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/service/api/api.service';
import { BaseComponent } from '../base/base.component';

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.scss']
})
export class StartComponent extends BaseComponent {

  public player_id_str = ''

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private api: ApiService,
    private router: Router,
  ) {
    super()
  }

  ngOnInit(): void {

  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  async onComfirmClicked() {
    let input_player_id = this.player_id_str ? parseInt(this.player_id_str) : -1
    let result = await this.api.checkPlayer(input_player_id)

    if (!result.isSuccess) {
      return
    }

    let game_id = result.body.game_id
    let player_id = result.body.player_id
    if (game_id) {
      let queryParams = {
        game_id,
        player_id,
      }
      this.router.navigate(['/wait'], { queryParams })
    }
    else {
      let queryParams = {
        player_id,
      }
      this.router.navigate(['/lobby'], { queryParams })
    }
  }
}
