// 🔹 Search Functionality for FIR
function initSearch() {
    const searchInput = document.querySelector('#search-input');
    const searchButton = document.querySelector('#search-button');
    const tableRows = document.querySelectorAll('.fir-table tbody tr');

    if (searchButton && searchInput) {
        searchButton.addEventListener('click', function () {
            const query = searchInput.value.trim().toLowerCase();
            console.log(`Searching for: ${query}`);

            tableRows.forEach(row => {
                const firDetails = row.textContent.toLowerCase();
                if (firDetails.includes(query)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }
}

// 🔹 Pagination Handling
function initPagination() {
    const rowsPerPage = 10;
    const tableRows = document.querySelectorAll('.fir-table tbody tr');
    const paginationContainer = document.querySelector('.pagination');

    function displayPage(pageNumber) {
        const start = (pageNumber - 1) * rowsPerPage;
        const end = start + rowsPerPage;
        
        tableRows.forEach((row, index) => {
            row.style.display = index >= start && index < end ? '' : 'none';
        });
    }

    if (paginationContainer) {
        const totalPages = Math.ceil(tableRows.length / rowsPerPage);
        paginationContainer.innerHTML = '';
        
        for (let i = 1; i <= totalPages; i++) {
            const pageButton = document.createElement('button');
            pageButton.textContent = i;
            pageButton.addEventListener('click', () => displayPage(i));
            paginationContainer.appendChild(pageButton);
        }
    }
    
    displayPage(1);
}

// 🔹 Table Actions (Edit/Delete)
function initTableActions() {
    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('edit-btn')) {
            console.log('Edit button clicked', e.target.dataset.id);
        } else if (e.target.classList.contains('delete-btn')) {
            console.log('Delete button clicked', e.target.dataset.id);
            if (confirm('Are you sure you want to delete this entry?')) {
                e.target.closest('tr').remove();
            }
        }
    });
}

// 🔹 Sample Data for Table
function initSampleData() {
    const tableBody = document.querySelector('.fir-table tbody');
    if (!tableBody) return;
    
    const sampleData = [
        { id: 1, case: 'Robbery', location: 'Downtown', status: 'Open' },
        { id: 2, case: 'Burglary', location: 'West Side', status: 'Closed' },
        { id: 3, case: 'Assault', location: 'East Side', status: 'Pending' }
    ];
    
    sampleData.forEach(data => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${data.id}</td>
            <td>${data.case}</td>
            <td>${data.location}</td>
            <td>${data.status}</td>
            <td>
                <button class="edit-btn" data-id="${data.id}">Edit</button>
                <button class="delete-btn" data-id="${data.id}">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// 🔹 Fetch Crime Statistics (Placeholder Function)
function fetchCrimeStatistics() {
    console.log('Fetching crime statistics...');
    // Simulating data fetch
    setTimeout(() => {
        console.log('Crime statistics loaded');
    }, 2000);
}
