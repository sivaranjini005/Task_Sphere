import { Component, inject } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-signup',
  imports: [ReactiveFormsModule],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {

  router = inject(Router);
  signupForm: FormGroup = new FormGroup({
    userName: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required, Validators.minLength(8)])
  });

  signUp() {
    if (this.signupForm.valid) {
      // Handle sign up logic here
      console.log('Signing up with', this.signupForm.value);
    }
  }

  goToLogin() {
    // Navigate to login page
    this.router.navigate(['/login']);
  }
}
