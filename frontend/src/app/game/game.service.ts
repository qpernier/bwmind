import { Injectable } from '@angular/core';
import { Urls } from '../constant';
import { HttpClient } from '@angular/common/http';
import { Pawn } from '../models/pawn';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Coord } from '../models/coord';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(private http: HttpClient, ) { }

  /**
   * Create new game
   */
  newGame(iaCode: string): Observable<Pawn[]> {
    return this.http.get<Pawn[]>(Urls.newGame + iaCode).pipe(
      map(pawnDict => {
        let pawnList = [];
        for (let pawn of pawnDict) {
          let allowedMoves = [];
          if (pawn['allowed_move'] !== null && pawn['allowed_move'] !== undefined) {
            for (let allowed_move_row of pawn['allowed_move']) {
              allowedMoves.push(new Coord(allowed_move_row["vertical_coord"], allowed_move_row["horizontal_coord"]))
            }
          }
          pawnList.push(new Pawn(pawn['id'], pawn['owner'], pawn['fk_game_id'], pawn['code'], pawn['vertical_coord'], pawn['horizontal_coord'], allowedMoves));
        }
        return pawnList;
      }),
    );
  }
}