import { ApiResponse } from "../api.service";

export class CreateGameResponse extends ApiResponse {

  body: CreateGameBody = {}

}

class CreateGameBody {

  game_id?: number

}
