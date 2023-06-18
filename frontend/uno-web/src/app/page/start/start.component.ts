import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/service/api/api.service';

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.scss']
})
export class StartComponent implements OnInit {

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private api: ApiService,
  ) { }

  ngOnInit(): void {
    this.api.createPlayer(1)
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  onComfirmClicked() {

  }
}
