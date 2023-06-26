import { ApiResponse } from "../api.service";

export class CheckPlayerResponse extends ApiResponse {

  body: CheckPlayerBody = {}

}

class CheckPlayerBody {

  game_id?: number
  player_id?: number

}
