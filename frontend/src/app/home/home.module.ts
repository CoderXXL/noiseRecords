import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UsersApiService } from '../services/users-api.service';
import { HttpClient } from '@angular/common/http';

@NgModule({
  declarations: [],
  imports: [CommonModule, HttpClient],
  providers: [UsersApiService]
})
export class HomeModule {}
