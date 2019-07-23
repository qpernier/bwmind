import { Injectable } from '@angular/core';
import { Urls } from '../constant';
import { HttpClient } from '@angular/common/http';
import { Pawn } from '../models/pawn';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(private http: HttpClient,) { }

  /**
   * Create new game
   */
  newGame(iaCode: string): Observable<Pawn[]>{
    return this.http.get<Pawn[]>(Urls.newGame + iaCode);
  }
}
