import { Injectable, inject } from '@angular/core';
import { TokenKeyName } from '../constants/constants';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  authenticationEvent$ = new BehaviorSubject<boolean>(false);
  authToken: string | null = '';
  router = inject(Router);

  logIn(userName: string, password: string): void {
    this.authToken = `${userName} ${password}`;
    localStorage.setItem(TokenKeyName, this.authToken);
    this.router.navigate(['/home']);
  }

  logOut(): void {
    this.authToken = null;
    localStorage.removeItem(TokenKeyName);
    this.router.navigate(['/login']);
  }

  checkIfAuthenticated() {
    return localStorage.getItem(TokenKeyName);
  }
}
