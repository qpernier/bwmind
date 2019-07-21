import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { GameComponent } from './game/game.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'game/:iaCode', component: GameComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}