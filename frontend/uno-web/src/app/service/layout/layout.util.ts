
export interface LayoutResult {
  target_width: number;
  target_height: number;
  target_x: number;
  target_y: number;
}

export function detectAndChangeLayout(): LayoutResult {
  document.documentElement.style.setProperty('--inner-width', `${document.documentElement.clientWidth}px`);
  document.documentElement.style.setProperty('--inner-height', `${document.documentElement.clientHeight}px`);

  const screenWidth = document.documentElement.clientWidth;
  const screenHeight = document.documentElement.clientHeight;
  // const targetRatio = 16 / 9;
  const targetRatio = 4 / 3;

  return changePageBox(screenWidth, screenHeight, targetRatio);
}

function changePageBox(width: number, height: number, targetRatio: number): LayoutResult {
  // 框線
  const currentRatio = width / height;
  // tslint:disable-next-line:variable-name
  let target_width = 0;
  // tslint:disable-next-line:variable-name
  let target_height = 0;
  if (currentRatio > targetRatio) {
    // width 太大 棄用
    target_width = height * targetRatio;
    target_height = height;
  }
  else {
    // height 太大 棄用
    target_width = width;
    target_height = width / targetRatio;
  }
  // this.target_w = target_width;
  // this.target_h = target_height;
  // console.log('layout w/h', target_width, target_height);
  document.documentElement.style.setProperty('--view-apply-width', `${target_width}px`);
  document.documentElement.style.setProperty('--view-apply-height', `${target_height}px`);

  // tslint:disable-next-line:variable-name
  let target_x = 0;
  // tslint:disable-next-line:variable-name
  let target_y = 0;
  // console.log('layout x/y', target_x, target_y);

  // this.target_x = target_x;
  // this.target_y = target_y;
  document.documentElement.style.setProperty('--view-apply-offset-x', `${target_x}px`);
  document.documentElement.style.setProperty('--view-apply-offset-y', `${target_y}px`);

  return {
    target_width,
    target_height,
    target_x,
    target_y,
  }
}
