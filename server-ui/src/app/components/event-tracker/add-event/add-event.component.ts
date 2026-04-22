import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-add-event',
  imports: [MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule, ReactiveFormsModule],
  templateUrl: './add-event.component.html',
  styleUrl: './add-event.component.css',
})
export class AddEventComponent {

    protected userForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<AddEventComponent>
  ) {
    this.userForm = this.fb.group({
      event_name: ['', Validators.required],
      event_date: ['', 
        [
          Validators.required, 
          Validators.pattern(/^(0[0-9]|[12][0-9]|3[01])$/) // Day of month: 01-31
        ]
      ],
      event_month: ['',
        [
          Validators.required,
          Validators.pattern(/^(0[0-9]|1[0-2])$/) // Month: 01-12
        ]
      ],
    });
  }

  // Method to save the form data and close the dialog
  protected save() {
    if (this.userForm.valid) {
      this.dialogRef.close(this.userForm.value);
    }
  }

  // Method to close the dialog without saving
  protected close() {
    this.dialogRef.close();
  }

}
