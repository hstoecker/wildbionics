import Cocoa
import WebKit
// usage: shot <url> <out.png> <width> [clipY clipH]  — screenshot via WebKit (full page, or a clip)
let a = CommandLine.arguments
let url = URL(string: a[1])!, out = a[2], w = CGFloat(Double(a[3])!)
let clip: (CGFloat, CGFloat)? = a.count > 5 ? (CGFloat(Double(a[4])!), CGFloat(Double(a[5])!)) : nil
class D: NSObject, WKNavigationDelegate {
  let wv: WKWebView; let win: NSWindow
  override init() {
    wv = WKWebView(frame: NSRect(x: 0, y: 0, width: w, height: 900))
    win = NSWindow(contentRect: wv.frame, styleMask: [.borderless], backing: .buffered, defer: false)
    super.init(); win.contentView = wv; wv.navigationDelegate = self; wv.load(URLRequest(url: url))
  }
  func webView(_ v: WKWebView, didFinish n: WKNavigation!) {
    DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
      // Offscreen WebKit freezes animations at frame 0 – disable them for the snapshot.
      v.evaluateJavaScript("var s=document.createElement('style');s.textContent='*,*::before,*::after{animation:none!important;transition:none!important}';document.head.appendChild(s);" + (ProcessInfo.processInfo.environment["SHOT_JS"] ?? "") + ";document.documentElement.scrollHeight") { r, _ in
        let h = CGFloat((r as? Double) ?? 900)
        self.win.setContentSize(NSSize(width: w, height: h)); v.frame = NSRect(x: 0, y: 0, width: w, height: h)
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
          let c = WKSnapshotConfiguration(); c.rect = clip.map { NSRect(x: 0, y: $0.0, width: w, height: min($0.1, h - $0.0)) } ?? NSRect(x: 0, y: 0, width: w, height: h); c.snapshotWidth = NSNumber(value: Double(w))
          if ProcessInfo.processInfo.environment["SHOT_PRINT_TITLE"] != nil { print(v.title ?? "") }
          v.takeSnapshot(with: c) { img, e in
            guard let img = img, let t = img.tiffRepresentation, let b = NSBitmapImageRep(data: t),
                  let p = b.representation(using: .png, properties: [:]) else { print(e ?? "fail"); exit(1) }
            try! p.write(to: URL(fileURLWithPath: out)); exit(0)
          }
        }
      }
    }
  }
}
let app = NSApplication.shared; app.setActivationPolicy(.prohibited)
let d = D(); app.run()
