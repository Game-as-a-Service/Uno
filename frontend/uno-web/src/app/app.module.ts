import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StartComponent } from './page/start/start.component';
import { LobbyComponent } from './page/lobby/lobby.component';
import { WaitComponent } from './page/wait/wait.component';
import { GameComponent } from './page/game/game.component';
import { FormsModule } from '@angular/forms'
import { ConfigServiceLoader } from './service/config/config.service.loader';

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
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
  ],
  providers: [
    ConfigServiceLoader,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
