import { Injectable } from '@angular/core';
import { Subject, fromEvent, interval, merge } from 'rxjs';
import { debounce } from 'rxjs/operators';
import { detectAndChangeLayout } from './layout.util';

@Injectable({
  providedIn: 'root'
})
export class LayoutService {

  private _updateStatus$ = new Subject<any>()

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor() {

    { // 創建訊號源
      let resize$ = fromEvent(window, 'resize')
      let orientationchange$ = fromEvent(window, 'orientationchange')
      let readystatechange$ = fromEvent(window, 'readystatechange')
      let fullscreenchange$ = fromEvent(document, 'fullscreenchange')
      merge(resize$, orientationchange$, readystatechange$, fullscreenchange$)
      .subscribe(this._updateStatus$);
    }
    { // 更新比例視窗
      this._updateStatus$
      .pipe(debounce(_ => interval(10)))
      .subscribe(() => {
        detectAndChangeLayout()
      })
    }
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  kickUpdate() {
    this._updateStatus$.next()
  }
}
