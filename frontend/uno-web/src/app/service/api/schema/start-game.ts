
import { ApiResponse } from "../api.service";

export class StartGameResponse extends ApiResponse {

  body: StartGameBody = {}

}
class StartGameBody {

  game_id?: number

}
