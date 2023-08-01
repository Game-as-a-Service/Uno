import { CardDTO, DeckDTO, PlayerDTO } from "src/app/service/api/schema/get-game-info";
import { CardColor, CardColors2DisplayStr, CardSymbol, CardSymbol2DisplayStr } from "src/app/util/const";


export class CardViewModel {

  player: PlayerDTO | undefined
  deck: DeckDTO | undefined

  getCardList() {
    let deck = this.deck
    if (!deck) {
      return []
    }
    return deck.card_list
  }

  getCardDisplayStr(dto: CardDTO) {

    let result = ''
    if (dto) {
      let color: CardColor = dto.color
      result += CardColors2DisplayStr[color]
      let symbol: CardSymbol = dto.symbol
      result += CardSymbol2DisplayStr[symbol]
    }

    return result
  }
}
