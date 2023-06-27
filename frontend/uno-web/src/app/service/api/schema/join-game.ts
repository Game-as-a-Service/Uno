
import { ApiResponse } from "../api.service";

export class JoinGameResponse extends ApiResponse {

  body: JoinGameBody = {}

}

class JoinGameBody {

    game_id?: number

}
