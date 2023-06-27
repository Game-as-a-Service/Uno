
export enum GameStates {
  unknown = -1,
  waiting = 1,
  preparing = 2,
  playing = 3,
  end = 4,
}

export const GameStates2DisplayStr = {

  [GameStates.unknown]: '未知',
  [GameStates.waiting]: '等待中',
  [GameStates.preparing]: '準備中',
  [GameStates.playing]: '遊玩中',
  [GameStates.end]: '已結束',

}

export enum CardColor {
  Unknown = -1,
  Blue = 1,
  Green = 2,
  Red = 3,
  Yellow = 4,
  Wild = 5,
}

export const CardColors2DisplayStr = {

  [CardColor.Unknown]: '未知',
  [CardColor.Blue]: '藍色',
  [CardColor.Green]: '綠色',
  [CardColor.Red]: '紅色',
  [CardColor.Yellow]: '黃色',
  [CardColor.Wild]: '萬用',
}

export enum CardSymbol {

  Unknown = -1,
  N0 = 0,
  N1 = 1,
  N2 = 2,
  N3 = 3,
  N4 = 4,
  N5 = 5,
  N6 = 6,
  N7 = 7,
  N8 = 8,
  N9 = 9,
  Skip = 10,
  Reverse = 11,
  DrawTwo = 12,
  Wild = 13,
  WildDrawFour = 14,
}

export const CardSymbol2DisplayStr = {

  [CardSymbol.Unknown]: '未知',
  [CardSymbol.N0]: '0',
  [CardSymbol.N1]: '1',
  [CardSymbol.N2]: '2',
  [CardSymbol.N3]: '3',
  [CardSymbol.N4]: '4',
  [CardSymbol.N5]: '5',
  [CardSymbol.N6]: '6',
  [CardSymbol.N7]: '7',
  [CardSymbol.N8]: '8',
  [CardSymbol.N9]: '9',
  [CardSymbol.Skip]: '跳過',
  [CardSymbol.Reverse]: '反轉',
  [CardSymbol.DrawTwo]: '抽兩張',
  [CardSymbol.Wild]: '萬用',
  [CardSymbol.WildDrawFour]: '萬用+抽四張',

}
