import { Component } from '@angular/core';
import { handleFileUpload } from '../shared/helper';
import { ViewerType } from '../shared/model';
import { viewers } from '../shared/demo-data';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  viewers = viewers;
  selectedViewer = this.viewers[0];
  selectedDoc = this.selectedViewer.docs[0];
  pdfSrc: any;

  selectViewer(viewerName: ViewerType) {
    if (viewerName !== this.selectViewer.name) {
      this.selectedViewer = this.viewers.find((v) => v.name === viewerName);
      this.selectedDoc = this.selectedViewer.docs[0];
    }
  }

  getDocExtension(doc: string) {
    const splittedDoc = doc.split('.');
    return splittedDoc[splittedDoc.length - 1];
  }

  async handleFiles(fileInput: any) {
    if (this.selectedViewer.name !== 'pdf'){
      this.selectedDoc = await handleFileUpload(fileInput);
      return;
    }
    const $img: any = document.querySelector('#input');

    if (typeof (FileReader) !== 'undefined') {
      const reader = new FileReader();

      reader.onload = (e: any) => {
        this.pdfSrc = e.target.result;
      };

      reader.readAsArrayBuffer($img.files[0]);
    }


  }
}
