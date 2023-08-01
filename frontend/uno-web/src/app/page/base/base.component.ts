import { AfterContentChecked, AfterContentInit, AfterViewChecked, AfterViewInit, Component, DoCheck, Input, OnChanges, OnDestroy, OnInit } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

@Component({
  selector: 'app-base',
  templateUrl: './base.component.html',
  styleUrls: []
})
export class BaseComponent implements
  OnChanges, OnInit, DoCheck,
  AfterContentInit, AfterContentChecked,
  AfterViewInit, AfterViewChecked,
  OnDestroy {

  protected ngUnsubscribe = new Subject<void>()

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  // https://ithelp.ithome.com.tw/articles/10188047

  constructor() { }

  ngOnChanges(): void { }

  ngOnInit(): void { }

  ngDoCheck(): void { }

  ngAfterContentInit(): void { }

  ngAfterContentChecked(): void { }

  ngAfterViewInit(): void { }

  ngAfterViewChecked(): void { }

  ngOnDestroy(): void {
    this.ngUnsubscribe.next()
    this.ngUnsubscribe.complete()
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  autoUnsubscribeObserver<OutputType>(observable: Observable<OutputType>): Observable<OutputType> {
    let result = observable
    .pipe(takeUntil(this.ngUnsubscribe))
    return result
  }
}
