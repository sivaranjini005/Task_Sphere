import { Component } from '@angular/core';
import { MainSectionComponent } from '../components/main-section/main-section.component';

@Component({
  selector: 'app-root',
  imports: [MainSectionComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'sphere-ui';
}
