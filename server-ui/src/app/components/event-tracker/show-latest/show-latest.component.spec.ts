import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowLatestComponent } from './show-latest.component';

describe('ShowLatestComponent', () => {
  let component: ShowLatestComponent;
  let fixture: ComponentFixture<ShowLatestComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ShowLatestComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowLatestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
