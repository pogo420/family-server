import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventTrackerComponent } from './event-tracker.component';

describe('EventTrackerComponent', () => {
  let component: EventTrackerComponent;
  let fixture: ComponentFixture<EventTrackerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EventTrackerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EventTrackerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
