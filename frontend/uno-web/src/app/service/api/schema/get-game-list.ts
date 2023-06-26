import { ApiResponse } from "../api.service";

export class GetGameListResponse extends ApiResponse {

  body: GetGameListBody = {
    game_id_list: []
  }

}

class GetGameListBody {
  game_id_list: number[] = []
}
