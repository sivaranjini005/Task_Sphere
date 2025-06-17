import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SphereRootComponent } from './sphere-root.component';

describe('SphereRootComponent', () => {
  let component: SphereRootComponent;
  let fixture: ComponentFixture<SphereRootComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SphereRootComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SphereRootComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
