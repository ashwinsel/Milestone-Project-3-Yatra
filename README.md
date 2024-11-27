# Yaatra - Spiritual Tours Guide
###### Code Institute / Backend for a web application using Python and a micro-framework / Milestone Project 3
[View Live Project Here][def42]

As a part of Milestone Project 3, this project demonstrates the use of non-relational databases with Flask and Python. The website serves as a platform where visitors can create and manage reviews about spiritual sites in India. It aims to foster a community of spiritual travelers, providing valuable insights and recommendations for future visitors.

### Purpose and Target Audience
The primary purpose of this platform is to connect spiritual travelers and cultural enthusiasts, offering a space to share and discover detailed reviews of spiritual journeys. By focusing on the unique aspects of spiritual and religious travel, the platform aims to stand out from other travel review websites.

![Screenshot][def24]

---

## **Index - Table of Contents**
------------

+ [User Experience (UX)](#-user-experience-ux)
    * [User Stories](#user-stories)             
+ [UX Planes](#ux-planes)
    * [Strategy](#strategy)
        - [Project Goals](#project-goals) 
        - [Customer Goals](#customer-goals)
        - [Company Goals](#company-goals)
        - [Future Implementations][def3]
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)     
    * [Surface](#surface)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
        - [Imagery](#imagery)
+ [Features](#features)
    * [Home Page](#home-page)
    * [Browse Site Page](#browse-site-page)
    * [Read Insights Page](#read-insights-page)
    * [Edit Sites page](#edit-sites-page)
    * [Edit Insights page](#edit-insights-page)
    * [Register Page](#register-page)           
+ [Traceability Matrix](#traceability-matrix)
+ [Logic](#logic)
+ [Database Structure](#database-structure)
+ [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
+ [Testing](#testing)
    * [Validator Testing Results](#validator-testing-results)
        
    * [Lighthouse Testing](#lighthouse-testing)
        
+ [Responsiveness Testing Results](#responsiveness-testing-results)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Browser Compatibility](#browser-compatibility)
+ [Deployment and Cloning](#deployment-and-cloning)
+ [Credits](#credits)
    * [Content](#content)
    * [Code](#code)
    * [Media](#media)
+ [Gratitude](#gratitude)

---

## **User Experience (UX)**

### **User Stories**

| **App Function**                    | **As a/an**                     | **I want to be able to...**                                 | **So that I can...**                                        |
|-------------------------------------|----------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **1. Viewing and Navigation**       | Visitor                         | Browse spiritual sites and journey insights                 | Explore potential destinations and learn from others' experiences |
|                                      | Visitor                         | View detailed information about a site                      | Understand the significance and plan my visit               |
|                                      | Visitor                         | Filter spiritual sites by region                   | Narrow down my search based on my specific interests        |
|                                      | Visitor                         | Search for a specific site or insight                       | Quickly find information about a particular location or experience |
|                                      | Visitor                         | Access the website on mobile or desktop devices             | Have a seamless browsing experience across devices          |
|                                      | Visitor                         | Navigate easily between pages       | Find the content I’m looking for without confusion          |
| **2. Registration and User Accounts** | Visitor                         | Register for an account                                      | Access features like adding, editing, or deleting entries   |
|                                      | Registered User                 | Log in to my account                                         | Manage my spiritual site entries and journey insights       |
|                                      | Registered User                 | Log out of my account                                        | Ensure my account information remains secure                |
| **3. Sites Management**              | Registered User                 | Add new spiritual sites                                      | Contribute to the database and help the community grow      |
|                                      | Registered User                 | Edit existing sites I created                               | Update or correct details for accuracy                      |
|                                      | Registered User                 | Delete sites I created                                       | Remove outdated or incorrect entries                        |
|                                      | Visitor                           | View all site submissions                                   | Learn about various sites and plan my travel             |
| **4. Insights Management**          | Registered User                 | Add a journey insight                                       | Share my travel experience and help others                  |
|                                      | Registered User                 | Edit insights I created                                     | Update or correct details of my reviews                     |
|                                      | Registered User                 | Delete insights I created                                   | Remove content that is no longer relevant                   |
|                                      | Visitor                         | View insights shared by others                              | Learn from the experiences of fellow travelers              |
| **5. Searching and Filtering**      | Visitor                         | Filter sites dynamically based on region and deity          | Easily find relevant sites that match my criteria           |
|                                      | Visitor                         | Search for a site by typing a keyword (e.g., deity name)    | Easily find relevant sites that match my criteria      |
| **6. Usability Enhancements**       | Visitor                         | View prominent links to "Browse Sites" and "Read Insights"  | Quickly access the main features of the site from the homepage |
|                                      | Visitor                         | Understand filtering instructions with clear prompts        | Avoid confusion when using input fields        |
| **7. Validation and Security**      | Registered User                 | Receive validation messages when filling forms              | Ensure I’m entering valid and complete information          |
| **8. Visual Design and Accessibility** | Visitor                         | Experience a visually appealing and accessible design       | Have an enjoyable and inclusive browsing experience         |
|                                      | Visitor                         | Use a consistent color scheme and typography               | Focus on content without distractions                       |

[Back to Index - Table of Contents](#index---table-of-contents)
---
## **UX Planes**
------------

### **Strategy**
The strategy focuses on creating a seamless platform to assist spiritual travelers in India. The Yatra app connects users to an extensive database of spiritual sites, enabling users to share insights, manage profiles, and plan tours effectively. It emphasizes accessibility, interactivity, and a community-driven model.

#### **Project Goals**
- **User Authentication:** Allow users to register, log in, and manage profiles securely.
- **Review Management:** Empower users to create, edit, and delete reviews of spiritual journeys.
- **Site Information Management:** Provide a platform to browse, filter, add, edit, and delete spiritual sites.
- **Inclusivity:** Ensure accessibility for users across all devices.
- **Filtering Capabilities:** Offer options to filter spiritual sites based on regions or deities.

#### **Customer Goals**
- **Visitors:** Access reviews and site information effortlessly to plan spiritual journeys.
- **Registered Users:** Create profiles, submit reviews, suggest sites, and manage content collaboratively.

#### **Future Implementations**
- **Social Media Integration:** Enable login and sharing features via Facebook and Twitter.
- **Expanding the Database:** Regularly update the platform with new spiritual sites and user-generated content.
- **Advanced Features:** Add forums, personalized travel itineraries, and AI-powered recommendations.

---

### **Scope**
The scope of the Yatra app ensures a comprehensive user experience with these core functionalities:

- **Review Insights:** Users can write, browse, and manage detailed journey reviews.
- **Site Information:** A vast list of spiritual sites is available, along with features to add, update, or delete information.
- **Filtering System:** Filters based on geographical regions and associated deities enhance navigation.
- **Navigation Bar:** A well-structured navigation bar ensures easy access to all features, including home, reviews and sites.
- **Interactive UI:** Features collapsible lists, modals, and sliders to present information in an engaging and accessible way.

---

### **Structure**
The structure organizes the app logically, focusing on intuitive navigation and efficient user interaction.

#### **Key Sections**
- **Home Page:** Welcomes users with a hero slider, navigation links, and introductory information about the app's purpose.
- **Browse Sites Page:** Lists spiritual sites with collapsible details, filters, and add/edit options (for logged-in users).
- **Read Insights Page:** Displays user-generated journey reviews in a grid layout, with edit/delete options for contributors.
- **Forms Section:** Includes forms for registration, login, site addition, and submit site reviews.
- **Search and Filter:** Provides a streamlined way to filter sites and reviews based on criteria like location and deity.

---

### **Skeleton**
The skeleton ensures a cohesive layout with responsive design principles.

#### **Wireframes**
1. **Home Page Wireframe:** Features a prominent hero section, call-to-action buttons, and informational cards.
![whomepage][def53]
2. **Browse Sites Page Wireframe:** Showcases a collapsible list of spiritual sites with filtering options.
![wbrowsesite][def54]
3. **Read Insights Page Wireframe:** Displays user insights in a responsive grid layout.
![wreviews][def55]
4. **Register Page Wireframe:** Displays a user registration form.
![wregister][def56]
5. **Login Page Wireframe:** Displays a user login form.
![wlogin][def57]

---

### **Surface**
The surface design reflects the spiritual essence of the Yatra app with a carefully chosen color palette, typography, and imagery.

#### **Color Scheme**
The color palette is inspired by India's spiritual richness, with hues that complement the banner imagery.

![Color Palette](./documentation/colour-pallete.png)

---

#### **Typography**
Typography reflects the balance between spiritual elegance and readability.

1. **'Lord Spirit':** 
   - Used exclusively for the brand logo in the navigation bar.
   - Styling: Font size of `3em`, paired with `#031929` (deep blue) for a visually striking contrast.

2. **'Lumanosimo':**
   - Applied globally for all body text and headings.
   - Styling: Subtle text shadow (`rgba(234, 194, 134, 0.5)`) enhances readability.

---

#### **Imagery**
1. **Banner Image:** An ethereal map of India featuring iconic spiritual landmarks. Represents the cultural and spiritual depth of the app's theme.
2. **Favicon:** A chakra-inspired icon symbolizing spiritual energy and mindfulness. Helps with easy identification in browser tabs.
3. **Other Images:** All images are compressed and optimized for performance, ensuring faster load times without compromising quality.

---

### **Future Goals**
The Yatra app has immense potential for growth. Here are some key goals for its future development:

#### **1. Gamification for Engagement**
   - Introduce reward points for active contributions like submitting reviews, adding new sites, or providing corrections. 
   - Create badges for milestones, such as "Top Reviewer" or "Explorer of the Month," to encourage consistent user engagement.

#### **2. Advanced AI Features**
   - Implement an **AI-based Recommendation System**:
     - Suggest spiritual sites based on user preferences, past reviews, and browsing history.
     - Provide personalized itineraries that combine multiple sites with travel routes, estimated travel times, and tips.
   - Incorporate **Natural Language Processing (NLP):**
     - Analyze user reviews to highlight commonly mentioned sentiments (e.g., “peaceful,” “crowded,” “beautiful architecture”).

#### **3. Mobile Application Development**
   - Expand the platform with a dedicated mobile app for iOS and Android users. This app can feature offline access to saved itineraries and reviews, ensuring usability in areas with limited internet connectivity.

#### **4. Community Forums and Discussions**
   - Introduce user forums where travelers can discuss topics like best travel times, local accommodations, and nearby restaurants.
   - Enable Q&A functionality, allowing users to seek advice from experienced travelers or moderators.

#### **5. Accessibility Enhancements**
   - Add support for more languages, catering to both domestic and international audiences.
   - Provide voice navigation and text-to-speech functionality for users with visual impairments.

#### **6. Enhanced Mapping Features**
   - Integrate with **Google Maps** or **Mapbox** for interactive mapping of spiritual sites.
   - Allow users to pin and save their favorite locations for future reference.

#### **7. Social Media Integration**
   - Enable users to share reviews, itineraries, and badges directly on platforms like Instagram, Twitter, and Facebook.
   - Allow registration and login using social media accounts for faster onboarding.

#### **8. API Development**
   - Develop APIs to allow third-party travel apps or tourism boards to integrate Yatra’s database of spiritual sites and reviews.

#### **9. Volunteer Moderation System**
   - Empower trusted users or moderators to review submitted content, ensuring that the platform remains reliable and user-driven.

#### **10. Donation and Sponsorship Model**
   - Introduce a donation system for users to support the platform's development.
   - Allow sponsorship opportunities for tour operators or religious organizations to highlight their services on the platform responsibly.

---

### **Conclusion**
The Yatra app is designed to empower spiritual travelers, providing an inclusive platform for sharing experiences, accessing resources, and fostering community engagement. With these future goals, Yatra aims to become a comprehensive tool for spiritual and cultural exploration, connecting travelers worldwide with India's spiritual heritage.

[Back to Index - Table of Contents](#index---table-of-contents)

---
## **Features**
---

### **Home Page**
#### 1. **Header Section with Slider**
   - **Dynamic Hero Slider (`.hslider`):**
     - The homepage features a dynamic slider with two slides designed to welcome users and highlight the purpose of "Yaatra."
     - **Slide 1:**
       - *Title*: "Yaatra" is prominently displayed with the tagline "Guide for Spiritual Travellers," reflecting the spiritual and community-oriented essence of the platform.
       - *Call-to-Actions*: For unauthenticated users, buttons for "Sign In" and "Register" are displayed prominently.
     - **Slide 2:**
       - *Title*: Encourages browsing by offering options to explore the site without logging in.
       - *Call-to-Actions*: "Browse Sites" and "Read Journey Insights" buttons facilitate navigation to key areas of the website.

#### 2. **Information Cards**
   - **Feature Highlights:**
     - A three-column grid displays cards explaining the core functionalities of the platform:
       - **About Us:** Introduces Yaatra's purpose and role in guiding spiritual travelers.
       - **Journey Insights:** Explains how users can share and benefit from shared travel experiences.
       - **Community Growth:** Emphasizes user participation in enriching the platform's offerings.

---

### **Browse Sites Page**
#### 1. **Header Section**
   - **Filter Options:**
     - Dropdown menus allow users to filter sites by:
       - **Region of India** (e.g., North, South, East, West).
       - **Deity** associated with the site.
     - A "Filter" button applies the chosen filters to display relevant results.
   - **Add Site Button:**
     - Visible to logged-in users, encouraging them to add new spiritual sites to the platform's growing database.

#### 2. **Collapsible List of Sites**
   - **Site Entries:**
     - Each site is displayed as a collapsible list item with:
       - *Site Name*: Bold text with an icon for temples.
       - *Accessibility*: A wheelchair icon indicates if the site is accessible for individuals with disabilities.
     - **Edit/Delete Options:**
       - Available only to the original creator of the site, providing secure content management.
   - **Detailed View:**
     - Upon expanding a site entry, users can view:
       - *Deity Name*, *Location*, and *Description* of the site.

---

### **Read Insights Page**
#### 1. **Header Section**
   - **Page Title:** 
     - "Journey Insights" is prominently displayed to set the page's theme.
   - **Add Insight Button:**
     - Logged-in users can click the "Add Insight" button to share their travel experiences.

#### 2. **Grid Layout of Insights**
   - **Insight Cards:**
     - Each card includes:
       - *Location Name*: The site being reviewed.
       - *Visit Date*: Clearly displayed for context.
       - *Purpose*: Explains the intent of the journey.
       - *Rating*: A user-provided score (0-5).
       - *Description*: A detailed review of the experience.
       - *Created By*: The author's username.
   - **Edit/Delete Buttons:**
     - Authors can edit or delete their reviews, ensuring up-to-date content.

---

### **Add Site Page**
#### 1. **Header Section**
   - Encourages users to contribute to the site database by sharing details about unlisted spiritual locations.

#### 2. **Form Features**
   - **Site Name Field:** 
     - Requires a valid site name (2-100 characters).
   - **Deity Field:**
     - Captures the primary deity's name (2-90 characters).
   - **Region Selector:**
     - Dropdown menu for selecting the geographical region.
   - **Description Field:**
     - A textarea for detailed site descriptions (5-800 characters).
   - **Disabled Access Checkbox:**
     - Allows users to indicate if the site is accessible for individuals with disabilities.
   - **Submit Button:**
     - Styled with an orange theme and icon for submission.

---

### **Add Insights Page**
#### 1. **Header Section**
   - Invites users to share their journey experiences for the benefit of the community.

#### 2. **Form Features**
   - **Location Field:**
     - Captures the name of the visited location (2-100 characters).
   - **Rating Field:**
     - Allows users to rate their experience (0-5 scale).
   - **Visit Date Field:**
     - A date picker for specifying the visit date.
   - **Purpose Field:**
     - Specifies the reason for the visit (e.g., retreat, prayer).
   - **Description Field:**
     - A textarea for a detailed review (5-800 characters).
   - **Submit Button:**
     - Prominent orange button styled for easy submission.

---

### **Edit Site Page**
#### 1. **Header Section**
   - Prompts users to refine or update information about an existing site entry.

#### 2. **Form Features**
   - Pre-filled fields allow users to easily update:
     - **Site Name**, **Deity**, **Region**, and **Description**.
   - **Disabled Access Checkbox:** 
     - Indicates whether the site is accessible for individuals with disabilities.
   - **Submit Button:** 
     - Styled for visibility and ease of use.

---

### **Edit Insights Page**
#### 1. **Header Section**
   - Encourages users to keep their insights up-to-date for the benefit of the community.

#### 2. **Form Features**
   - Allows users to edit previously submitted:
     - **Location Name**, **Rating**, **Visit Date**, **Purpose**, and **Description**.
   - **Submit Button:** 
     - Prominent orange button for submission.

---

### **Authentication Pages**
#### **Login Page**
   - **Username and Password Fields:** 
     - Collect login credentials with validation for security.
   - **Submit Button:** 
     - Initiates the login process.
   - **Register Link:** 
     - Redirects users to the registration page if they don’t have an account.

#### **Register Page**
   - **Form Fields:**
     - Collects username, password, and password confirmation.
   - **Validation:** 
     - Ensures matching passwords and username constraints are met.
   - **Register Button:** 
     - Submits the registration request.

[Back to Index - Table of Contents](#index---table-of-contents)

------------
- ## **Logic**
    * The initial flowchart designed to base the app routes is as follows:
    ![Flowchart][def25]
    * The final Flowchart prepared using Draw.io based on all app routes
    ![Flowchart2][def35]

    * Deatiled step by step logic in English. Detailed flow aligns with the logic implemented in app.py and provides a comprehensive overview of how the Yatra app functions end-to-end.
      #### Steps in Yatra App Functionality

        ###### **User Visits Homepage (/)**

        The app loads the homepage, displaying site information and navigation options based on the user's login status.

        **Features:**
        - **If logged out:** Options to log in or register.
        - **If logged in:** Personalized options such as profile management, browsing, or adding content.

        ---

        ###### **User Registration (/register)**

        - Users can register by providing a unique username and a password.
        - Validation ensures no duplicate usernames and confirms the password.
        - **On successful registration:**
          - A user session is created.
          - Redirects to the user's profile page.

        ---

        ###### **User Login (/login)**

        - Users provide their credentials to log in.
        - Validates the username and password against the database.
        - **On success:**
          - A user session is created.
          - Redirects to the user's profile page.
        - **On failure:**
          - Displays a flash error message.

        ---

        ###### **User Logout (/logout)**

        - Clears the user's session.
        - Redirects back to the login page with a flash message confirming the logout.

        ---

        ###### **Browse Spiritual Sites (/browse_sites)**

        Displays a list of spiritual sites from the database.

        **Features:**
        - **Filter options:**
          - Filter by geographical regions or associated deities.
        - **Search functionality:**
          - Supports case-insensitive and partial matches.
        - **For logged-in users:**
          - Add, edit, or delete site entries based on ownership.

        ---

        ###### **Add a New Site (/add_site)**

        - Accessible only to logged-in users.
        - Users fill out a form to provide:
          - Site name, associated deity, geographical region, description, and accessibility features.
        - Validates all fields before submission.
        - **On success:**
          - Adds the new site to the database.
          - Redirects to the browse sites page with a success message.

        ---

        ###### **Edit an Existing Site (/edit_site/<locations_id>)**

        - Accessible only to the site's creator.
        - Allows the user to update:
          - Site name, associated deity, region, description, and accessibility status.
        - Validates all input fields.
        - **On success:**
          - Updates the database.
          - Redirects to the browse sites page.

        ---

        ###### **Delete a Site (/delete_site/<locations_id>)**

        - Accessible only to the site's creator.
        - Deletes the specified site from the database.
        - Redirects to the browse sites page with a confirmation message.

        ---

        ###### **Read Insights (/read_insights)**

        Displays user reviews or journey insights.

        **Features:**
        - Organized in a grid format, showing:
          - Site name, date of visit, rating, purpose, and detailed review.
        - Logged-in users can edit or delete their own reviews.

        ---

        ###### **Add a New Insight (/add_insights)**

        - Accessible only to logged-in users.
        - Users provide:
          - Site visited, rating, visit date, purpose, and review description.
        - All fields are required, and validation ensures proper formatting.
        - **On success:**
          - Adds the new review to the database.
          - Redirects to the read insights page.

        ---

        ###### **Edit an Existing Insight (/edit_insights/<review_id>)**

        - Accessible only to the review's creator.
        - Allows users to update their review details.
        - Validates all fields.
        - **On success:**
          - Updates the database.
          - Redirects to the read insights page.

        ---

        ###### **Delete an Insight (/delete_insights/<review_id>)**

        - Accessible only to the review's creator.
        - Deletes the specified review from the database.
        - Redirects to the read insights page with a confirmation message.

        ---

        ###### **Search and Filter Functionality**

        - Available on the browse sites and read insights pages.
        - **Supports case-insensitive partial matches for:**
          - Deity names.
          - Geographical regions.
        - Returns dynamically updated results.

        ---

        ###### **Dynamic Dropdowns (/get_part_names)**

        - Fetches distinct geographical regions dynamically for dropdown filters.
        - Enhances user experience by providing only relevant options.

        ---

        ###### **Error Handling**

        - All routes implement error handling for:
          - Invalid IDs for editing or deleting entries.
          - Missing or empty form fields.
          - Unauthorized access attempts.

        ---

        ###### **Session Management**

        - Sessions are used to manage user authentication.
        - Restricts features like adding, editing, or deleting entries to logged-in users.

[Back to Index - Table of Contents](#index---table-of-contents)

------------ 
## **Database Structure**

The Yatra application uses a non-relational database (MongoDB) to manage its data. The data is structured into collections, each serving a specific purpose for the application functionality. Below is a detailed explanation of the collections, their fields, and relationships.

---

### **Collections and Schema**

#### 1. **`locations` Collection**
Stores information about various spiritual sites listed on the platform.

- **Fields:**
  - `site_name` (String): The name of the spiritual site.
  - `deity` (String): The deity associated with the site.
  - `part_name` (String): The geographical region of the site (e.g., North India, South India).
  - `description` (String): Detailed description of the site, its significance, and features.
  - `access` (Boolean): Indicates whether the site is wheelchair accessible.
  - `created_by` (String): Username of the user who added the site.

- **Relationships:**
  - Linked to the `user` collection via the `created_by` field, which matches the `username` of the user who created the entry.
  - Reviews for a site are stored in the `reviews` collection, related by the `site_name` field.

---

#### 2. **`user` Collection**
Contains user credentials and manages authentication.

- **Fields:**
  - `username` (String): Unique username of the user.
  - `password` (String): Hashed password for secure storage.

- **Relationships:**
  - Users are linked to the `locations` collection (via `created_by`) and the `reviews` collection (via `created_by`) to track ownership of sites and reviews.

---

#### 3. **`part` Collection**
Stores distinct region names for dropdown filtering in forms.

- **Fields:**
  - `part_name` (String): Name of the geographical region.

- **Relationships:**
  - Used in the `locations` collection as a filter criterion via the `part_name` field.

---

#### 4. **`reviews` Collection**
Holds user-generated reviews or journey insights about the sites.

- **Fields:**
  - `where` (String): Name of the site reviewed.
  - `rating` (Number): User rating of the experience (e.g., 1-5).
  - `visit_date` (Date): Date of the visit.
  - `purpose` (String): Purpose of the visit (e.g., pilgrimage, meditation).
  - `review_des` (String): Detailed review description.
  - `created_by` (String): Username of the user who created the review.

- **Relationships:**
  - Linked to the `locations` collection via the `where` field, which matches the `site_name`.
  - Linked to the `user` collection via the `created_by` field.

---

### **Schema ER Diagram**
![erdiagram][def36]

------------    
## **Technologies Used**
------------

### **Languages Used**
- **HTML5**: Used for structuring the application's content with semantic and accessible markup.
- **CSS3**: Provides styling and layout for the application's user interface, including responsive designs and animations.
- **JavaScript (with JQuery)**: Enhances interactivity and dynamic functionality, enabling efficient DOM manipulation and AJAX calls.
- **Python**: Powers the backend logic, enabling server-side processing, routing, and integration with the database.

---

### **Frameworks, Libraries, and Programs Used**

- **[Cdnfonts](https://www.cdnfonts.com/)**: Used to import the 'Samarkan' font into the `style.css` file, which is applied to the main logo title for aesthetic appeal.
- **[Font Awesome](https://fontawesome.com/)**: Integrated to provide icons for better user experience and visual enhancement throughout the website.
- **[Git](https://git-scm.com/)**: Utilized for version control, allowing changes to be tracked and committed via the Gitpod terminal before being pushed to the repository.
- **[GitHub](https://github.com/)**: Used as the hosting platform for the project's repository, enabling code sharing and collaboration.
- **[Balsamiq](https://balsamiq.com/)**: Employed to create wireframes during the design phase, ensuring a clear layout and structure of the application before development.
- **[Coolors](https://coolors.co/)**: Assisted in generating a complementary color palette that aligns with the background image, ensuring a visually harmonious design.
- **[Materialize CSS](https://materializecss.com/)**: Utilized for responsive front-end design, including buttons, sliders, card panels, and navigation menus to enhance the user interface.
- **[Autoprefixer CSS Online](https://autoprefixer.github.io/)**: Parsed the `style.css` file to add necessary browser prefixes, ensuring compatibility across different browsers.
- **[favicon.io](https://favicon.io/)**: Used to create the favicon for the application, providing branding and recognition in browser tabs.
- **[W3C Markup Validation Service](https://validator.w3.org/)**: Verified the validity of the HTML and CSS code for all pages, ensuring adherence to web standards and best practices.
- **[UI.Dev](https://ui.dev/)**: Generated mockup screenshots to visualize and present the website’s layout and design in real-world scenarios.
- **[Free Formatter](https://www.freeformatter.com/)**: Used to format and indent HTML and CSS code properly for improved readability and maintainability.
- **[MongoDB](https://www.mongodb.com/)**: Implemented as the database to store and manage application data, such as user details, locations, and reviews.

---

### **Additional Tools**
- **Tinypng**: Optimized images for better performance and faster page load times.
- **Lighthouse Testing (Chrome DevTools)**: Evaluated performance, accessibility, best practices, and SEO, ensuring the application delivers a high-quality experience.
- **Heroku**: Hosted and deployed the application, providing a robust and scalable environment for the project.
- **Drawio**: Create flowchart and ER diagram

This stack of technologies ensures a seamless development process and delivers a highly functional, accessible, and visually appealing web application for the "Yatra" platform.

    
- ## **Testing**
------------

### **Test Cases Used for Testing Features**

#### **Home Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_HM_001         | Hero Slider          | Verify the hero slider displays both slides.                    | Both slides appear with correct content and buttons.       |
| TC_HM_002         | Login/Register Button| Check if the login/register buttons redirect correctly.         | User is redirected to the login or register page.          |
| TC_HM_003         | Browse Sites Button  | Verify the "Browse Sites" button works for unauthenticated users.| User is redirected to the Browse Sites page.               |

---

#### **Register Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_RG_001         | Username Field       | Validate that the username field accepts only alphanumeric input.| Validation error appears for invalid input.                |
| TC_RG_002         | Password Matching    | Verify that the password confirmation matches the entered password.| Validation error appears if passwords do not match.        |
| TC_RG_003         | Registration Process | Test successful registration with valid data.                   | User is redirected to the profile page with a success message.|

---

#### **Login Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_LG_001         | Login Form           | Validate login with correct credentials.                        | User is redirected to the profile page.                    |
| TC_LG_002         | Invalid Credentials  | Test login with incorrect credentials.                          | Error message appears, and login fails.                    |
| TC_LG_003         | Empty Fields         | Verify that login fails if fields are left blank.               | Validation error appears, and login fails.                 |

---

#### **Browse Sites Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_BS_001         | Filter by Region     | Test filtering sites by region.                                 | Only sites from the selected region are displayed.          |
| TC_BS_002         | Filter by Deity      | Test filtering sites by deity.                                  | Only sites associated with the selected deity are displayed.|
| TC_BS_003         | Add Site Button      | Verify the "Add Site" button redirects correctly for logged-in users.| User is redirected to the Add Site page.                   |

---

#### **Add Site Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_AS_001         | Site Name Validation | Validate that the site name field does not accept special characters.| Validation error appears for invalid input.                |
| TC_AS_002         | Accessibility Checkbox | Test if the wheelchair accessibility checkbox works.            | The checkbox updates the site's accessibility status.       |
| TC_AS_003         | Successful Submission| Verify form submission with valid data.                         | Site is added to the database, and user is redirected to the Browse Sites page.|

---

#### **Edit Site Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_ES_001         | Pre-filled Fields    | Verify that fields are pre-filled with existing site details.    | All fields are populated with correct data.                |
| TC_ES_002         | Validation on Update | Validate input fields when updating site details.                | Validation error appears for invalid input.                |
| TC_ES_003         | Update Confirmation  | Verify site details are updated successfully.                   | Site is updated, and user is redirected to the Browse Sites page.|

---

#### **Read Insights Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_RI_001         | Insights Grid Display| Test that insights are displayed in a grid format.              | Insights appear as grid items with appropriate fields.      |
| TC_RI_002         | Edit/Delete Buttons  | Verify that edit/delete buttons appear only for the insight creator.| Buttons are visible only for the creator of the insight.   |

---

#### **Add Insight Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_AI_001         | Required Fields      | Verify that all fields are marked as required.                  | Validation error appears if any required field is empty.    |
| TC_AI_002         | Successful Submission| Verify form submission with valid data.                         | Insight is added to the database, and user is redirected to the Read Insights page.|

---

#### **Edit Insight Page**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_EI_001         | Pre-filled Fields    | Verify that fields are pre-filled with existing insight details. | All fields are populated with correct data.                |
| TC_EI_002         | Validation on Update | Validate input fields when updating insight details.             | Validation error appears for invalid input.                |
| TC_EI_003         | Update Confirmation  | Verify insight details are updated successfully.                | Insight is updated, and user is redirected to the Read Insights page.|

---

#### **Delete Functionality**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_DEL_001        | Delete Site          | Verify that a site can be deleted only by its creator.           | Site is deleted, and user is redirected to the Browse Sites page.|
| TC_DEL_002        | Delete Insight       | Verify that an insight can be deleted only by its creator.       | Insight is deleted, and user is redirected to the Read Insights page.|

---

#### **Search and Filter**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_SF_001         | Search by Deity      | Test search functionality for deities (case-insensitive).        | Relevant results are displayed dynamically.                |
| TC_SF_002         | Search by Region     | Test search functionality for regions (case-insensitive).        | Relevant results are displayed dynamically.                |

---

#### **Dynamic Dropdowns**
| **Test Case ID** | **Feature**           | **Test Description**                                            | **Expected Result**                                         |
|-------------------|-----------------------|------------------------------------------------------------------|------------------------------------------------------------|
| TC_DD_001         | Fetch Regions        | Verify that dropdown dynamically fetches distinct regions.       | Dropdown updates with only relevant options.               |

[Back to Index - Table of Contents](#index---table-of-contents)

---

### Manual Testing (Feature Testing)

#### Authentication

| Sr No | Page       | User Action                                    | Expected Result                                               | Pass/Fail |
|-------|------------|-----------------------------------------------|--------------------------------------------------------------|-----------|
| 1     | Register   | Enter valid username and password, click 'Register'. | User is redirected to the profile page.                      | Pass      |
| 2     | Register   | Enter an existing username and click 'Register'.     | Error message displayed: "Username already exists."          | Pass      |
| 3     | Register   | Enter mismatched passwords and click 'Register'.     | Error message displayed: "Passwords do not match."           | Pass      |
| 4     | Login      | Enter valid username and password, click 'Login'.    | User is redirected to the profile page.                      | Pass      |
| 5     | Login      | Enter invalid username or password, click 'Login'.   | Error message displayed: "Incorrect Username and/or Password." | Pass    |
| 6     | Logout     | Click 'Logout'.                                    | User is redirected to the login page.                        | Pass      |

---

#### Visitor Features

| Sr No | Page           | User Action                                   | Expected Result                                                | Pass/Fail |
|-------|----------------|----------------------------------------------|---------------------------------------------------------------|-----------|
| 7     | Navbar         | Click on the Yatra logo.                     | Redirected to the home page.                                  | Pass      |
| 8     | Browse Sites   | Search with a valid site name.               | List of matching locations displayed.                         | Pass      |
| 9     | Browse Sites   | Leave the search input blank and click 'Search'. | User is redirected to the browse-sites page.                  | Pass      |
| 10    | Browse Sites   | Use 'Part of India' filter dropdown.          | Locations filtered based on selected region.                  | Pass      |
| 11    | Browse Sites   | Search using deity name (case insensitive).   | List of locations matching the deity displayed.               | Pass      |

---

#### User Features

| Sr No | Page            | User Action                                  | Expected Result                                                | Pass/Fail |
|-------|-----------------|----------------------------------------------|----------------------------------------------------------------|-----------|
| 12    | Add Site        | Add a site with all required fields filled.  | Site is added successfully, and user is redirected to browse-sites. | Pass  |
| 13    | Add Site        | Add a site with missing fields.              | Error message displayed: "All fields are required."            | Pass      |
| 14    | Edit Site       | Update all fields of an existing site.       | Updates are saved, and user is redirected to browse-sites.     | Pass      |
| 15    | Delete Site     | Click 'Delete' button on a site.             | A confirmation dialog appears: "Are you sure you want to delete this site? This action cannot be undone." On confirmation, the site is deleted. | Pass |
| 16    | Add Insight     | Add an insight with valid details.           | Insight is saved, and user is redirected to insights page.     | Pass      |
| 17    | Add Insight     | Submit an insight form with missing fields.  | Error message displayed: "All fields are required."            | Pass      |
| 18    | Edit Insight    | Update all fields of an existing insight.    | Changes are saved, and user is redirected to insights page.    | Pass      |
| 19    | Delete Insight  | Click 'Delete' button on an insight.         | A confirmation dialog appears: "Are you sure you want to delete this insight? This action cannot be undone." On confirmation, the insight is deleted. | Pass |

---

#### Defensive Programming

| Sr No | Feature         | Implementation                              | Expected Result                                                | Pass/Fail |
|-------|-----------------|---------------------------------------------|----------------------------------------------------------------|-----------|
| 20    | Delete Site     | Confirmation prompt before deletion.        | Dialog box prevents accidental deletion.                       | Pass      |
| 21    | Delete Insight  | Confirmation prompt before deletion.        | Dialog box prevents accidental deletion.                       | Pass      |

[Back to Index - Table of Contents](#index---table-of-contents)

---

+ ### Validator Testing Results
    * Css was validated using https://jigsaw.w3.org/css-validator/#validate_by_input+with_options
      The CSS validation report confirms that no major errors were found in the stylesheet; the document successfully validates as CSS Level 3 + SVG. However, the following warnings were noted:

      Vendor Extensions: Properties such as -webkit-box, -ms-flexbox, and related attributes are flagged as vendor-specific extensions. These are included to ensure cross-browser compatibility for flexbox layouts and other advanced CSS features.

      Imported Stylesheets: Imported fonts from external sources (Lord Spirit and Lumanosimo) were not validated in the direct input mode. This is standard behavior as external files are excluded from the validation process.

      Grid and Flex Properties: Some CSS grid and flex properties, such as -ms-grid and -webkit-box-flex, are marked as vendor-specific warnings.

      Resolution:
      The vendor-specific warnings are expected and necessary for ensuring cross-browser compatibility. They do not impact the functionality or appearance of the website and are therefore ignored.

      ![cssvalidateresult][def39]

    * HTML Validation Results Using W3C Validator
      Validation Outcome:

      The document passed the validation with no errors or warnings for all pages but for Login and Register page.

      This confirms that the HTML code adheres to the standards set by the W3C, ensuring proper semantic structure and compliance.

      As seen below the Logina nd Register page showed 2 errors which are explained as follows:
      1. Error: No Digits After ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*@$!%*?.
          Cause:
          This error occurs because the pattern attribute for password validation contains special characters like @$!%*?&# directly within the regex without proper escaping. The validator expects a stricter syntax or escape sequences.
          Impact:
          The regex validation may still work in most browsers, but it is flagged by validators as it doesn't strictly conform to HTML5's expected encoding of special characters in regex patterns.
      2. Error: No Digits After &#])[A-Za-z\d@$!%*?.
          Cause:
          Similar to the first error, this issue arises due to the unescaped inclusion of &# in the regex, which is misinterpreted as an incomplete HTML entity instead of part of the regex pattern.
          Impact:
          Like the first issue, the functionality is not impacted in modern browsers, but it fails validation standards.
      
      ![homepagevalidatorresult][def43]
      ![browsesitesvalidatorresult][def44]
      ![readinsightsvalidatorresult][def48]
      ![loginvalidatorresult][def51]
      ![registervalidatorresult][def52]
    
    * Javascript was tested using JSHint
      The JSHint validation of the script.js file highlights the following metrics and findings:

      The file contains 9 functions, with the largest function having 13 statements and the most complex function having a cyclomatic complexity of 3, which is within acceptable limits for maintainable code based on results in Stack Overflow entries.
      One unused variable (jQuery) was identified on line 2. This likely results from declaring jQuery as a global variable but not directly referencing it within the script.
      Action Taken:
      The unused jQuery variable does not affect functionality since $ (the alias for jQuery) is actively used throughout the code. The declaration was included to satisfy the JSHint validation for $ (based on a response on Stack Overflow), so this warning can be safely ignored.

      ![jsvalidateresult][def41]

    * app.py python code passed the Code Institute Linter for Python.
        The Python validation results for the Yatra app's python code showed no errors or warnings. This indicates that the python code is syntactically correct and compliant with Pep8 standards.

      ![pythonvalidateresult][def38]
    

[Back to Index - Table of Contents](#index---table-of-contents)

+ ### Lighthouse Testing Results

| Page           | Performance | Accessibility | Best Practices | SEO  | Observations                                                                                      |
|-----------------|-------------|---------------|----------------|------|--------------------------------------------------------------------------------------------------|
| Browse Sites   | 94          | 86            | 100            | 100  | Good performance and SEO. Accessibility could be improved to ensure a seamless user experience. |
| Home Page      | 99          | 87            | 100            | 100  | Excellent performance and SEO. Accessibility can benefit from further adjustments.              |
| Read Insights  | 95          | 92            | 100            | 100  | Strong performance and accessibility with minimal layout shifts ensuring a smooth experience.   |
| Register Page  | 99          | 95            | 100            | 100  | Near-perfect metrics across all categories. Accessibility is well-optimized.                   |
| Sign-In Page   | 99          | 95            | 100            | 100  | Excellent metrics with no significant improvements needed.                                      |
| Add Insight    | 94          | 93            | 100            | 100  | Minor layout improvements could further enhance the user experience.                            |
| Add Site       | 95          | 81            | 100            | 100  | Strong performance. Accessibility score highlights areas for enhancement, like form labels.     |

### Findings
1. **Performance**: All pages scored above 90, indicating optimized load times and minimal rendering delays.
2. **Accessibility**: Scores vary between 81 and 95, suggesting improvements are needed, especially for form field labels and contrast issues.
3. **Best Practices**: All pages scored a perfect 100, reflecting adherence to web standards and secure development practices.
4. **SEO**: Scores were consistently at 100, demonstrating excellent optimization for search engines.

Results
![HomePage][def50]
![BrowseSites][def64]
![ReadInsight][def65]
![Register][def66]
![SignIn][def67]
![AddInsight][def68]
![AddSite][def47]

[Back to Index - Table of Contents](#index---table-of-contents)

+ ### Responsiveness Testing Results
    #### HomePage Page
    ![Results][def26]
    #### Browse Sites Page
    ![Results][def27]
    #### Registration Page
    ![Results][def30]
    #### Login Page
    ![Results][def31]
    #### Read Insights Page
    ![Results][def32]

[Back to Index - Table of Contents](#index---table-of-contents)

---

## **Bugs and Fixes**

**1. Issue with Dynamic Dropdown Behavior in "Select Part of India"**
Bug Encountered: The dropdown for "Select Part of India" required users to manually click "Apply Filters" once to load options dynamically. This behavior was unintuitive, and users often did not understand why the dropdown was empty.

Root Cause: The dropdown relied on backend data fetched asynchronously but lacked an automated trigger or preloading mechanism.

Resolution: A dedicated /get_part_names route was created to fetch the dropdown data dynamically. JavaScript AJAX was used to trigger this call on page load, ensuring the dropdown was populated seamlessly without user intervention.

**2. Continuous Triggering of Filters on Page Load**
Bug Encountered: Auto-triggering the "Apply Filters" button caused continuous loops of the action, leading to poor performance and usability.

Root Cause: The JavaScript lacked proper state management, resulting in infinite event triggering.

Resolution: A triggered flag was introduced to ensure the button auto-triggered only once. This resolved the infinite loop issue and ensured the button remained functional for manual usage.

**3. Case Sensitivity and Limited Flexibility in Deity Filtering**
Bug Encountered: The "Select Deity" dropdown restricted users to predefined options, which did not support partial or case-insensitive searches. This made it difficult for users to filter based on personalized inputs.

Root Cause: The backend query relied on exact matches, which excluded valid results with slight variations in spelling or case (e.g., "Shiva" vs. "shiva").

Resolution: The dropdown was replaced with a free-text input field. Validation was added to ensure clean inputs (pattern="^[a-zA-Z0-9 ]{2,90}$"). The backend was enhanced to use MongoDB's $regex operator with case-insensitive matching, allowing more flexible filtering.

**4. Delete Functionality Did Not Work Consistently**
Bug Encountered: The delete functionality for both sites and journey insights did not always remove the correct entries. This led to confusion and created data inconsistencies.

Root Cause: Improper usage of ObjectId during deletion attempts caused invalid MongoDB queries, resulting in no action being taken.

Resolution: Validation was added to ensure that valid ObjectId values were passed to the delete queries. Error handling was also improved to provide clear feedback when deletions failed due to invalid or missing IDs.

**5. Edit Functionality Validation**
Bug Encountered: Users could submit incomplete or invalid data when editing entries, leading to malformed or broken records in the database.

Root Cause: Validation for required fields was either absent or improperly implemented in the frontend forms and backend routes.

Resolution: Comprehensive validation logic was added to both the frontend and backend to ensure all fields were filled out before submission. Backend logic was adjusted to reject invalid updates and provide informative error messages.

**6. Usability Enhancements: Adding Links to Home Page**
Bug Encountered: The homepage did not include intuitive navigation links to key sections like "Browse Sites" and "Journey Insights," forcing users to navigate through the top menu.

Root Cause: A lack of design foresight during the initial UI implementation.

Resolution: Hyperlinks were added to the "Browse Sites" and "Journey Insights" cards on the homepage. These links guide users directly to the respective sections, improving the overall navigation experience.

**7. Visual Enhancements: Color and Typography**
Bug Encountered: The application had inconsistent typography and color schemes across pages, leading to a lack of visual coherence. Important messages and elements lacked sufficient contrast, reducing readability.

Root Cause: Colors and typography were not aligned with a consistent design system during the initial implementation.

Resolution: The color scheme was standardized across the application, using contrasting tones for text and backgrounds to improve readability. Typography was adjusted for consistency and emphasis, with clear headings and appropriate font sizes for different sections.

**8. Cluttered "Read Insights" Page**
Bug Encountered: The "Read Insights" page displayed all journey details at once, overwhelming users and making it difficult to scan through entries.

Root Cause: The UI lacked an expandable or collapsible design, forcing users to scroll through unnecessary details for each entry.

Resolution: A collapsible structure was implemented, showing only the title, visit date, and rating by default. Additional details can be revealed by clicking on a specific entry. This improvement streamlined the layout and made it easier to navigate.

**9. Missing Validation for Materialize Select**
Bug Encountered: The select elements on the filter and form pages failed validation when users interacted with them improperly or skipped them entirely, even for optional fields.

Root Cause: Materialize select elements required additional logic to handle focus, blur, and selection states.

Resolution: Custom validation logic was implemented using JavaScript to dynamically mark select elements as valid or invalid based on user interaction. This ensured smoother form submission and reduced user frustration.

**10. Reset Button Behavior on Filters**
Bug Encountered: Clicking the "Reset" button did not fully clear the form fields or reload the page state. This caused filters to behave unpredictably after being reset.

Root Cause: The reset button was not programmed to reinitialize the dropdowns or clear backend queries.

Resolution: The "Reset" button was configured to reload the page entirely, ensuring that all filters were cleared and dropdowns were reset to their default states.

[Back to Index - Table of Contents](#index---table-of-contents)

---
- ## Browser Compatibility
------------
* Testing has been carried out on the following browsers :
    - Chrome Version 120.0.6099.225 (Official Build) (64-bit)
    - Firefox Version 122.0 (64-bit)
    - Edge Version 121.0.2277.83 (Official build) (64-bit)
    All the functionalities and appearance works as intended on all the above browsers.

- ## Deployment and Cloning
------------- 
+ Deployment to Heroku:

    * Open a command line/terminal window within the main project folder. 
    * Create a requirements.txt file by typing `pip3 freeze --local > requirements.txt` at the command line.
    * Create a Procfile by typing `echo web: python app.py > Procfile` 
    * Add and commit these files to Github.
    * Go to (https://www.heroku.com/). Log in or create an account
    * Click the 'New' button and click 'Create new app'.
    * Enter a unique name for your project with no capital letters or spaces and select the region closest to you (e.g., Europe). Click 'Create App'.
    * Inside the dashboard for your new app, go to the 'Settings' tab. 
    * Scroll down and click 'Reveal Config Vars' then enter data for the following variables:
    - `IP : 0.0.0.0`
    - `PORT : 5000`
    - `MONGO_DBNAME : ...` Your MongoDB database name
    - `MONGO_URI : ...` Your MongoBD URI (found on MongoDB by going to Clusters > Connect > Connect to your application)
    - `SECRET_KEY : ...` Your secret key
    * Link Github repo to Heroku by navigating to the Deploy tab. Select 'GitHub, enter the name of the repository and click connect. 
    * Once connected, select the repo branch to deploy (e.g. main) then click the Enable Automatic Deployment option.
    * To deploy immediately, in the Manual Deploy section again select the branch you want to deploy and click Deploy Branch. This will retrieve the code from GitHub. Once this is complete you'll receive a message "Your app was successfully deployed." You can then click "View" to access the deployed app.
    * 


+ Cloning:

    * visit url - https://github.com/ashwinsel/Milestone-Project-2 this will open the repository on Github
    * Click on the "Code" green coloured button to the right of the screen, click HTTPs and copy the link there
    * Open a GitBash terminal and navigate to the directory where you want to locate the clone
    * On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process

- ## Credits
------------
- ### Content
    * Some inputs regarding sites has been adapted from https://www.visa-indian-online.org/the-full-guide-to-spiritual-tourism-in-india 
    ![def33]
    * All other content has been drafted by the developer.

- ### Code
    * Code on how to present a modal and close was created with the help of a tutorial on [WebDevSimplified][def76].
    * Code for the hover effect on info cards on Home page was an play around with some examples from  [Codepen]
    * I have used Materialize code to implement various aspects of the website.
    * The basic logic has been based on a tutorial by Tim Nelson, Task Manager Walkthrough.
    * Hover effects on throughout has been created by using tutorials on [W3schools](https://www.w3schools.com/cssref/sel_hover.php)
    * Datepicker aspect and some other code adapted from Task Manager Walkthourgh on Code Institute by Tim Nelson
    * Slider code was inspired by Hitesh Choudhary

- ### Media
    * ![Favicon]![def4] a vector art by https://www.shutterstock.com/g/iostephy
    * [Background Image]![def46]

- ## Gratitude
    * I would like to thank my mentor Dick Vlaanderen for all the coaching and helping me with their insight and experience.
    * Thanks to tutor Rebecca and Alan, who helped me fix my connection to MOngoDB.
    * Thank you to Hitesh Chaudhary for the lessons on ChaiCode.com.
    * Thanks to various contributors on StackOverflow.
    * Thanks to Amy our facilitator for running our regular Stand-ups which gave me confidence.
    * Thanks to Code with Harry on tutorial videos re Python and PyMongo






[Cdnfonts]: https://www.cdnfonts.com/samarkan.font
[def0]: https://travelmoves.in/india-news/indias-travel-trends-surge-in-spiritual-destination-searches
[def1]: ./documentation/favicon.png
[def2]: #c-frequent-user-goals
[def3]: #future-implementations
[def4]: https://www.shutterstock.com/g/iostephy
[def6]: ./documentation/validatorresults.png
[def7]: ./documentation/firstlighthouseresult.png
[def8]: ./documentation/lighthousetesting2.png
[def9]: https://fontawesome.com/
[def10]: https://ashwinsel-milestone1-shxwdq7nqt6.ws-eu107.gitpod.io/
[def11]: https://github.com/ashwinsel/Milestone-1.git
[def12]: https://www.microsoft.com/en-gb/microsoft-365/powerpoint
[def13]: https://balsamiq.com/
[def14]: https://coolors.co/
[def15]: https://tinypng.com/
[def16]: ./documentation/testcasesandresults.png
[def17]: https://materializecss.com/about.html
[def18]: https://autoprefixer.github.io/
[def19]: https://favicon.io/
[def20]: https://validator.w3.org/
[def21]: https://linktr.ee/iamavinashkr
[def22]: https://ui.dev/amiresponsive?url=https://ashwinsel.github.io/Milestone-1/index.html
[def23]: https://www.freeformatter.com/html-formatter.html
[def24]: ./documentation/ss-home.png
[def25]: ./documentation/flowchart1.png
[def26]: ./documentation/ss-home.png
[def27]: ./documentation/ss-browsesites.png
[def28]: ./documentation/ss-addinsight.png
[def29]: ./documentation/colour-pallete.png
[def30]: ./documentation/ss-register.png
[def31]: ./documentation/ss-signin.png
[def32]: ./documentation/ss-readinsight.png
[def33]: https://www.visa-indian-online.org/the-full-guide-to-spiritual-tourism-in-india
[def34]: ./documentation/error1.png 
[def35]: ./documentation/flowchart.png
[def36]: ./documentation/erdiagram.png
[def37]: ./documentation/whomepage.png
[def38]: ./documentation/py-validate-result.png
[def39]: ./documentation/cssvalidate-ss.png
[def40]: ./documentation/W3C-CSS-Validator-results.pdf
[def41]: ./documentation/jsvalidate-ss.png
[def42]: https://yatra1-4cc0076860db.herokuapp.com/ 
[def43]: ./documentation/valsshome.png
[def44]: ./documentation/valssbrowsesites.png
[def45]: ./documentation/lt-addsite.png
[def46]: ./documentation/main-img.png
[def47]: ./documentation/lt-addsite.png
[def48]: ./documentation/valssreadinsights.png
[def49]: ./static/img/chakra.png
[def50]: ./documentation/lt-home.png
[def51]: ./documentation/valsslogin.png
[def52]: ./documentation/valssregister.png
[def53]: ./documentation/whome.png
[def54]: ./documentation/wbrowsesites.png
[def55]: ./documentation/wreviews.png
[def56]: ./documentation/wregister.png
[def57]: ./documentation/wlogin.png
[def64]: ./documentation/lt-browsesites.png
[def65]: ./documentation/lt-readinsight.png
[def66]: ./documentation/lt-register.png
[def67]: ./documentation/lt-signin.png
[def68]: ./documentation/lt-addinsight.png
[def75]: https://www.jagranjosh.com/general-knowledge/gk-quiz-on-hindu-mythology-1706194424-1
[def76]: https://courses.webdevsimplified.com/