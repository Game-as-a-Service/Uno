import { Component, Input, OnInit, Output } from '@angular/core';
import { CardViewModel } from '../share/card.viewmodel';

// https://yabeline.tw/Stickers_Data.php?Number=3232447
@Component({
  selector: 'app-main-card',
  templateUrl: './main-card.component.html',
  styleUrls: ['./main-card.component.scss']
})
export class MainCardComponent implements OnInit {

  @Input()
  viewModel: CardViewModel | undefined

  constructor() { }

  ngOnInit(): void {
  }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
  
}
