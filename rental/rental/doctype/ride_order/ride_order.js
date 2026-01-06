frappe.ui.form.on("Ride Order", {
    onload(frm) {
        console.log("running load...");
    },
    setup(frm) {
        console.log("setup...");
    },
    refresh(frm) {
        console.log("on refresh...");

        // Agar status "Accepted" nahi hai, tabhi button dikhao
        if (frm.doc.status !== "Accepted") {
            frm.add_custom_button("Accept", () => {
                // Status ko "Accepted" set karo
                frm.set_value("status", "Accepted");
                // Form ko save karo
                frm.save();
            });
        }
    },
});
