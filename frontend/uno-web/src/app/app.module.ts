import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StartComponent } from './page/start/start.component';
import { LobbyComponent } from './page/lobby/lobby.component';
import { WaitComponent } from './page/wait/wait.component';
import { GameComponent } from './page/game/game.component';

@NgModule({
  declarations: [
    AppComponent,
    StartComponent,
    LobbyComponent,
    WaitComponent,
    GameComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
