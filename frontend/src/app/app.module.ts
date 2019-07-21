import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import {ButtonModule} from 'primeng/button';
import {DialogModule} from 'primeng/dialog';
import { HttpClientModule } from '@angular/common/http';
import {RadioButtonModule} from 'primeng/radiobutton';
import { FormsModule } from '@angular/forms';
import { GameComponent } from './game/game.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    GameComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    ButtonModule,
    DialogModule,
    HttpClientModule,
    RadioButtonModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
