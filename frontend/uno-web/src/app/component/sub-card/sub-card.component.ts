import { Component, Input, OnInit, Output } from '@angular/core';
import { CardViewModel } from '../share/card.viewmodel';

@Component({
  selector: 'app-sub-card',
  templateUrl: './sub-card.component.html',
  styleUrls: ['./sub-card.component.scss']
})
export class SubCardComponent implements OnInit {

  @Input()
  viewModel: CardViewModel | undefined

  constructor() { }

  ngOnInit(): void {
  }

}
