import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { NgxDocViewerComponent } from './document-viewer/document-viewer.component';
@NgModule({
  imports: [CommonModule],
  declarations: [NgxDocViewerComponent],
  exports: [NgxDocViewerComponent]
})
export class SharedModule {}
