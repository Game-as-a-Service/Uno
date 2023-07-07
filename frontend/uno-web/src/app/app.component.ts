import { Component } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ConfigService } from './service/config/config.service';
import { LayoutService } from './service/layout/layout.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  constructor(
    private title: Title,
    private layout: LayoutService,
  ) {
    this.title.setTitle(ConfigService.useSetting.lobby.title)
    this.layout.kickUpdate()
  }
}
