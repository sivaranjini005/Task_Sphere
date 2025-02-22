import { CanActivateFn, Router } from '@angular/router';
import { AuthenticationService } from '../services/authentication.service';
import { inject } from '@angular/core';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthenticationService);
  const router = inject(Router);

  // Check if the user is authenticated
  if (authService.checkIfAuthenticated()) {
    return true; // Allow route activation
  } else {
    // Redirect to login page if not authenticated
    router.navigate(['/login']);
    return false; // Block route activation
  }
};
