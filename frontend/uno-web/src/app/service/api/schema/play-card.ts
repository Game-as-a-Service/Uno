
import { ApiResponse } from "../api.service";

export class PlayCardResponse extends ApiResponse {

    body: PlayCardBody = {}

}

class PlayCardBody {

  game_id?: number
  
}
