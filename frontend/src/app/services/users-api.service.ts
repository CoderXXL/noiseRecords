import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../env';
import { User } from '../users/user.model';

@Injectable()
export class UsersApiService {
  constructor(private http: HttpClient) {}

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(
      err.message || 'Error: Unable to complete request.'
    );
  }

  getUsers(): Observable<any> {
    return this.http
      .get(`${API_URL}/users`)
      .pipe(catchError(UsersApiService._handleError));
  }
}
