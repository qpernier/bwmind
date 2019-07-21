import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

  iaCode: string = null;

  board: string[][] = [];

  constructor(private route: ActivatedRoute) {
    this.buildBoard();

  }

  buildBoard(){
    for (let i = 0; i < 8; i++) {
      let ligne: string[] = [];
      for (let y = 0; y < 8; y++) {
        if(i % 2 == 0){
          if (y % 2 == 0) {
            ligne.push('black');
          } else {
            ligne.push('white');
          }
        }else{
          if (y % 2 == 0) {
            ligne.push('white');
          } else {
            ligne.push('black');
          }
        }
      }
      this.board.push(ligne);
    }
    console.log(this.board);
  }

  ngOnInit() {
    this.iaCode = this.route.snapshot.paramMap.get('iaCode');
  }

}
