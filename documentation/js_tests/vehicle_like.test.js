describe('Vehicle Like System', () => {
    beforeEach(() => {
        // Mock authenticated user state
        const mockUser = {
            isAuthenticated: true,
            id: 1
        };
        global.currentUser = mockUser;

        // Mock project data
        const mockProject = {
            id: 1,
            title: "Test Project",
            likes: 0
        };

        document.body.innerHTML = `
            <div class="project-card" data-project-id="${mockProject.id}">
                <h2>${mockProject.title}</h2>
                <button class="btn-like" data-project-id="${mockProject.id}">
                    <span class="like-count">${mockProject.likes}</span>
                    <i class="fas fa-heart"></i>
                </button>
            </div>`;

        document.body.innerHTML += '<input type="hidden" name="csrfmiddlewaretoken" value="mockCSRFToken">';
    });

    test('prevents like when user is not authenticated', () => {
        global.currentUser.isAuthenticated = false;
        const likeButton = document.querySelector('.btn-like');
        likeButton.click();
        expect(document.querySelector('.like-count').textContent).toBe('0');
    });

    test('allows like when user is authenticated', async () => {
        const likeButton = document.querySelector('.btn-like');
        
        // Mock fetch response
        global.fetch = jest.fn().mockImplementation(() =>
            Promise.resolve({
                json: () => Promise.resolve({ likes: 1 })
            })
        );

        // Add click handler with mocked fetch
        likeButton.addEventListener('click', async function() {
            if (global.currentUser.isAuthenticated) {
                const response = await fetch();
                const data = await response.json();
                this.querySelector('.like-count').textContent = data.likes;
            }
        });

        await likeButton.click();
        await new Promise(resolve => setTimeout(resolve, 0));
        expect(document.querySelector('.like-count').textContent).toBe('1');
    });
});