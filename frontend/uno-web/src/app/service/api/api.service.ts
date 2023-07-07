import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { timeout } from 'rxjs/operators';
import { CheckPlayerResponse } from './schema/check-player';
import { CreateGameResponse } from './schema/create-game';
import { JoinGameResponse } from './schema/join-game';
import { GetGameListResponse } from './schema/get-game-list';
import { GetGameInfoResponse } from './schema/get-game-info';
import { StartGameResponse } from './schema/start-game';
import { PlayCardResponse } from './schema/play-card';
import { ConfigService } from '../config/config.service';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  host = '' // http://localhost:5000

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private http: HttpClient,
  ) {
    this.host = ConfigService.useSetting.lobby.api
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  async checkPlayer(player_id: number): Promise<CheckPlayerResponse> {
    let path = `${this.host}/game/check_player`
    let header = {}
    let body = {
      player_id
    }
    return this.convenientPost(path, body, header)
  }

  async createGame(): Promise<CreateGameResponse> {
    let path = `${this.host}/game/create_game`
    let header = {}
    let body = {
      game_id: -1
    }
    return this.convenientPost(path, body, header)
  }

  async joinGame(game_id: number, player_id: number): Promise<JoinGameResponse> {
    let path = `${this.host}/game/join_game`
    let header = {}
    let body = {
      game_id,
      player_id,
    }
    return this.convenientPost(path, body, header)
  }

  async getGameList(): Promise<GetGameListResponse> {
    let path = `${this.host}/game/get_game_list`
    let header = {}
    let body = {}
    return this.convenientPost(path, body, header)
  }

  async getGameInfo(game_id: number): Promise<GetGameInfoResponse> {
    let path = `${this.host}/game/get_game_info`
    let header = {}
    let body = {
      game_id
    }
    return this.convenientPost(path, body, header)
  }

  async startGame(game_id: number, player_id: number): Promise<StartGameResponse> {

    let path = `${this.host}/game/start_game`
    let header = {}
    let body = {
      game_id,
      player_id,
    }
    return this.convenientPost(path, body, header)
  }

  async playCard(game_id: number, player_id: number, index: number): Promise<PlayCardResponse> {
    let path = `${this.host}/game/play_card`
    let header = {}
    let body = {
      game_id,
      player_id,
      index,
    }
    return this.convenientPost(path, body, header)
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  async convenientPost(
    path: string,
    body: any = {},
    headers: any = {},
    waitTime: number = 1500,
  ): Promise<ApiResponse> {
    // debug(`api path: %o body: %o`, path, body);
    // console.log('api', path);

    let newBody = Object.assign({
      present: "json"
    }, body)

    const data = await this.http.post(path, newBody, { headers }).pipe(timeout(waitTime))
      .toPromise()
      .catch(this.handleError);

    let res = new ApiResponse()
    res.body = data
    return res;
  }

  private handleError(error: any): Promise<ApiResponse> {
    console.log('Api error', error);

    let res = new ApiResponse()
    res.isError = true
    res.error = error

    return Promise.resolve(res);
  }
}

export class ApiResponse {

  isError = false
  body: any = {}
  error: any = {}

  get isSuccess() {
    return this.body?.isSuccess ?? false
  }
  get errorMsg() {
    return this.body?.error ?? ''
  }
}
