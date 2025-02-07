document.getElementById('supplierForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const supplierName = document.getElementById('supplier_name').value;
    const code = generateCode(supplierName);
    document.getElementById('result').innerText = `Generated Code: ${code}`;
});

function generateCode(supplierName) {
    const cleanedName = supplierName.replace(/[^A-Za-z]/g, '');
    let initials = cleanedName.split('').map(word => word[0]).join('');
    while (initials.length < 5) {
        initials += cleanedName.charAt(Math.floor(Math.random() * cleanedName.length));
    }
    return `SU${initials.slice(0, 5).toUpperCase()}`;
}