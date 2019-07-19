import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  displayDialogIASelection: boolean = false;

  constructor() { }

  ngOnInit() {
  }

  onShowDialog(){
    this.displayDialogIASelection = true;
  }

  /**
   * Handle click on the start playing button
   */
  onStart(){
    //TODO
  }
}
