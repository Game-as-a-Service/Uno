import { ApiResponse } from "../api.service";

export class GetGameInfoResponse extends ApiResponse {

  body: GetGameInfoBody = {} as any

}

interface GetGameInfoBody {
  game_id: number
  game_states: number
  host: number
  player_list: PlayerDTO[]
  deck_list: DeckDTO[]
}

export interface PlayerDTO {
  id: number
}

export interface DeckDTO {
  player_id: number
  card_list: CardDTO[]
}

export interface CardDTO {
  symbol: number
  color: number
}
