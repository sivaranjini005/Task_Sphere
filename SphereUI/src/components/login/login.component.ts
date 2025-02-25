import { Component, inject } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { AuthenticationService } from '../../services/authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  authenticationService: AuthenticationService = inject(AuthenticationService);
  router = inject(Router);

  loginForm: FormGroup = new FormGroup({
    userName: new FormControl('', Validators.required),
    password: new FormControl('', [Validators.required, Validators.minLength(8)])
  });

  logIn() {
    this.authenticationService.logIn(this.loginForm.value.userName, this.loginForm.value.password);
  }

  goToSignUp() {
    this.router.navigate(['/signup']);
  }
}
