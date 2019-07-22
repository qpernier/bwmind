import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Square } from '../models/square';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

  /** Code of the playing IA */
  iaCode: string = null;

  /** Represent the borad
   *  7:0 * * * * * * 7:7
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *   *  * * * * * *  *
   *  0:0 * * * * * * 0:7
   */
  board: Square[] = [];

  /**Square size in px   */
  squareSize = 100;

  constructor(private route: ActivatedRoute) {
    this.buildBoard();

  }

  /**Build the board */
  buildBoard(){
    for (let i = 0; i < 8; i++) {
      for (let y = 0; y < 8; y++) {
        // 7-1 to convert vertical coord to top
        let vertical_coord = (7-i)*this.squareSize;
        let horizontal_coord = y*this.squareSize;
        if(i % 2 == 0){
          if (y % 2 == 0) {
            this.board.push(new Square('black', vertical_coord, horizontal_coord));
          } else {
            this.board.push(new Square('white', vertical_coord, horizontal_coord));
          }
        }else{
          if (y % 2 == 0) {
            this.board.push(new Square('white', vertical_coord, horizontal_coord));
          } else {
            this.board.push(new Square('black', vertical_coord, horizontal_coord));
          }
        }
      }
    }
    console.log(this.board);
  }

  ngOnInit() {
    this.iaCode = this.route.snapshot.paramMap.get('iaCode');
  }

}
