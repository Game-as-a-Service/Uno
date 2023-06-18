import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/service/api/api.service';

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.scss']
})
export class StartComponent implements OnInit {

  public player_id = ''

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private api: ApiService,
  ) { }

  ngOnInit(): void {

  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  async onComfirmClicked() {
    if (!this.player_id) {
      this.api.checkPlayer(-1)
    }
    else {
      this.api.checkPlayer(parseInt(this.player_id))
    }
  }
}
