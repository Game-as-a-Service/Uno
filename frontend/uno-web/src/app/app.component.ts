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

  scale = 1;

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  constructor(
    private title: Title,
    private layout: LayoutService,
  ) {
    this.title.setTitle(ConfigService.useSetting.lobby.title)

    this.layout.result.subscribe(result => {
      // 算出縮放倍率
      // console.log('layout result', result)
      // 因為寬高比一樣 只要算寬 1440 1080
      if (result) {
        this.scale = result.target_width / 1440
      }
    })

    this.layout.kickUpdate()
  }
}
