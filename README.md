# Yaatra - Spiritual Tours Guide
###### Code Institute / Back end for a web application using Python and a micro-framework. / Milestone Project 3
------------
[View Live Project Here][def42]

As a part of Milestone Project 3 to demonstrate an understanding of on non-relational databases using Flask and Python. I have developed a website that serves as a platform where visitors can create and manage reviews about spiritual sites in India. This platform aims to foster a community of spiritual travellers, providing valuable insights and recommendations for future visitors.

Purpose and Target Audience
The primary purpose of this platform is to connect spiritual travellers, tour operators, and cultural enthusiasts, offering a space to share and discover detailed reviews of spiritual journeys. By focusing on the unique aspects of spiritual and religious travel, the platform aims to stand out from other travel review websites.

![Screenshot][def24]

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
    * [Quiz Landing Page](#quiz-landing-page)
        - [F1.1 Guide](#f11-guide)
        - [F1.2 Music Toggle Button](#f12-music-toggle-button)
        - [F1.3 Reset Button](#f13-reset-button)
        - [F1.4 Question Box](#f14-question-box)
        - [F1.5 Answer option buttons x 4](#f15-answer-option-buttons-x-4)    
        - [F1.6 Next Button](#f21-next-button)
        - [F1.7 Score Display Box](#f17-score-display-box)
        - [F1.8 Instructions MOdal](#f18-instructions-modal)       
+ [Traceability Matrix](#traceability-matrix)
+ [Logic](#logic)
+ [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
+ [Testing](#testing)
    * [Validator Testing Results](#validator-testing-results)
        
    * [Lighthouse Testing](#lighthouse-testing)
        - [First Results](#first-results)
        - [Final Results](#final-results)
+ [Test Cases and Results](#test-cases-and-results)
+ [Responsiveness Testing Results](#responsiveness-testing-results)
+ [BUgs and Fixes](#bugs-and-fixes)
+ [Browser Compatibility](#browser-compatibility)
+ [Deployment and Cloning](#deployment-and-cloning)
+ [Credits](#credits)
    * [Content](#content)
    * [Code](#code)
    * [Media](#media)
+ [Gratitude](#gratitude)

## **User Experience (UX)**
------------

- ### User stories
As a User from all different age groups and technical abilities I want the website not to be complicted and too busy.
1. **User Registration**
   - *As a new visitor, I want to create an account to access all the website features.*
   - *As a registered user, I want to log in to my account to manage my site entries and journey insights.*
2. **Creating Journey Insights**
   - *As a registered user, I want to create a review of a journey so that I can share my experiences with others. *
3. **Editing and Deleting Reviews**
   - *As a registered user, I want to edit my reviews so that I can update my experiences or correct any mistakes.*
   - *As a registered user, I want to delete my reviews so that I can remove any content I no longer wish to share.*
4. **Adding New Spiritual Sites**
   - *As a registered user, I want to add information about new spiritual sites that are not listed on the website so that I can contribute to the community’s knowledge base.*
5. **Browsing Sites and Routes**
   - *As a visitor, I want to browse a list of spiritual sites to explore potential places to visit.*
   - *As a visitor, I want to browse a list of regular routes so that I can plan my journeys more effectively.*
6. **Suggesting Journey Insights**
   - *As a registered user, I want to share insights that connect specific religious sites so that I can help others with their travel planning.*
7. **Reading Reviews**
   - *As a visitor, I want to read experiences of other travelers so that I can make informed decisions about my travels.*
8. **User Recommendations**
   - *As a registered user, I want to recommend sites and insights based on my experiences so that I can help other users have better journeys.*
9. **Responsive Design**
    - *As a visitor, I want the website to be responsive so that I can access it on any device, including my mobile phone or tablet.*
10. **Search Functionality**
    - *As a visitor, I want to search for specific spiritual sites, tour operators, or routes so that I can quickly find the information I need.*
11. **Sites Sorting and Filtering**
    - *As a visitor, I want to sort and filter reviews based on criteria like date, rating, and popularity so that I can easily find the most relevant information.*
    
## **UX Planes**
------------
- ### **Strategy**
    * Make it easier for users planning a tour to spiritual destinations around India. Provide a platform for sharing reviews of tour operators and spiritual sites in India. Facilitate community engagement and knowledge sharing.
    + #### Project Goals
    * This includes User Authentication: Registration, login, profile management. Review Management: Create, edit, update and delete journey insights. Site Information: Create, edit, update and delete spiritual sites, browse existing sites. Filter spiritual sites based on certain attributes.
    * Being able to access all devices.
    + #### Customer Goals
    * The focus is on meeting the needs of users, both first-time visitors and returning users. 
    * Visitors: Access reviews, browse spiritual sites, and plan travel routes.
    * Registered Users:** Create and manage profiles, submit and edit reviews, suggest new sites and routes.
    + #### Future Implementations
    * Additional Social Media Integrations: Integrating other platforms like Facebook and Twitter for broader user engagement. Expanded Database: Continuously updating the database with more spiritual sites and user-generated content. Advanced Features: Implementing features like user forums, travel itineraries, and recommendation algorithms to enhance user experience.
- ### **Scope**
    - The scope of the Yaatra website encompasses creating a user-friendly and accessible web interface that allows users to:
        * Users can create and manage their profiles. Only the profile owner can edit or delete their reviews, ensuring authenticity and control.
        * Users can write detailed reviews about their experiences with tour operators, routes taken, and spiritual sites visited.
        * Users can contribute information about new spiritual sites that are not yet listed on the platform, enriching the database.
        * Users can browse through an extensive list of potential spiritual sites to visit.
        * Users can add and suggest possible routes that connect specific religious sites, helping others plan their journeys.
- ### **Structure**
    - The Structure Plane outlines how the information and functionalities are organized.
        * Home Page: Introduction, Navigation to other parts, Option to Register or just Browse.
        * Sites Section: List of sites, add new site, update or delete a site.
        * Insights Page: Create review, browse reviews, review details.
        * Navigation: Top navigation bar with links to Home, Reviews, Sites, Routes, Profile, and Admin (if applicable).
        * Forms: Registration, login, review submission, site and route suggestion forms.
        * Search and Filter: Search bar and filters for reviews, sites, and routes.
- ### **Skeleton**
    + #### Wireframes
        ![Home Page Wireframe][def4]
        ![Events Page Wireframe][def5]                    
- ### **Surface**
    + #### Colour Scheme
        * I have used a rusted copper ztar color palette consistent with the backgorund image of a ethereal map image.
        * #CD8D47 a shade of dark green, black, and a dark rusty font colors play a good contrast to the chosen colour palette.

        ![Colour Scheme][def29]        

    + #### Typography
        ### Typography Used in the CSS

1. **Fonts Imported:**
   - **'Lord Spirit':** Imported from `https://fonts.cdnfonts.com/css/lord-spirit`.
   - **'Lumanosimo':** Imported from `https://fonts.cdnfonts.com/css/lumanosimo`.

2. **Font Families Applied:**
   - **'Lumanosimo', sans-serif:** Applied globally to the entire body, ensuring that the text throughout the website is primarily set in this font.
   - **'Lord Spirit', sans-serif:** Specifically used for the `.brand-logo` in the navigation bar to give it a distinctive and visually striking appearance.

### Detailed Write-Up

#### 1. **'Lumanosimo' Font:**
   - **Usage:** 
     - This font is the primary typeface for the website and is applied globally across most of the text elements, such as the body text and `.banner-text`. It ensures consistency and coherence in the visual language of the site.
   - **Styling:**
     - The font is paired with a sans-serif fallback to maintain legibility in cases where the custom font fails to load.
     - Additionally, text shadows are applied to the body text using `text-shadow: 2px 2px 2px rgba(234, 194, 134, 0.5);`. This effect adds depth and a subtle glow to the text, enhancing its readability against varied backgrounds.

#### 2. **'Lord Spirit' Font:**
   - **Usage:** 
     - This font is exclusively used for the `.brand-logo` in the navigation bar. The large size (`font-size: 3em;`) and unique styling of 'Lord Spirit' create a distinct identity for the brand name, making it stand out on the page.
   - **Styling:**
     - The font is paired with a sans-serif fallback to maintain consistency in appearance and ensure that the brand logo remains visually appealing, even if the custom font is not available.
     - The font color is set to `#031929`, a dark blue that contrasts well with the background, ensuring that the logo is easily recognizable.

### Typography Implementation

The chosen typography reflects the spiritual and elegant nature of the "Yaatra Spiritual Tours Guide" website. 

- **'Lumanosimo'** provides a balance between readability and a touch of sophistication, suitable for the descriptive and narrative content of the website. The text-shadow effect enhances the spiritual and ethereal feel, which aligns with the theme of spiritual tours.
  
- **'Lord Spirit'** contributes to brand recognition by making the logo striking and memorable. Its decorative style is likely intended to evoke a sense of tradition and cultural richness, which resonates with the spiritual focus of the site.

* Responsive Design Considerations

- The font sizes are adjusted in the media queries to ensure readability across different screen sizes. For instance, the brand logo's font size decreases on smaller screens (`2em` for tablets and `1.5em` for mobile devices), maintaining visual hierarchy without overwhelming the smaller display areas.
- Similarly, the `.banner-text` and button text sizes are reduced on smaller screens to ensure the layout remains clean and accessible, avoiding text overflow and maintaining a harmonious design.
    + #### Imagery
        ![backgroundimage][def46]
        *   This image is ideal for use in the banner or hero section of your website, especially on the homepage. The vibrant and captivating visual of iconic Indian landmarks symbolizes spirituality, culture, and the essence of India's spiritual heritage, perfectly aligning with the theme of "Yaatra Spiritual Tours Guide."
        * ![favicon][def49] The favicon was designed using an online favicon generator. This has been designed with an image that has a man sat inbetween coloured aura and chakra through. This makes it to able to spot amongst several tabs in the browser.
        * All the images used are license free or been used with owners consent. The sources are listed in the Credits section.
        * Images used were compressed using Tinypng.com for better performance and user experience.

## **Features**
------------
- ### Home page
#### 1. **Header Section with Slider**
   - **Hero Slider (`.hslider`):**
     - The homepage opens with a dynamic slider, featuring two distinct slides that introduce users to the core offerings of "Yaatra" – a guide for spiritual travelers.
     - **Slide 1:** 
       - *Title*: "Yaatra" - The site title is displayed in an elegant and grand font, 'Lord Spirit,' emphasizing the spiritual essence of the platform. The large font size (6rem) ensures the title is the focal point, grabbing the user's attention immediately.
       - *Tagline*: "Guide for Spiritual Travellers" - This succinct tagline conveys the purpose of the platform, helping visitors understand what the website is about at a glance.
       - *Call to Action*: 
         - If the user is not logged in, they see options to either "Sign In" or "Register," each button styled with a teal darken-1 background, ensuring they stand out against the banner's background. Icons like the sign-in and user-plus symbols enhance usability and visual appeal.
     - **Slide 2:**
       - *Title*: "Just want to Browse?" - This slide addresses users who may not want to sign up immediately, offering an inviting alternative to explore the site.
       - *Tagline*: "No Problem!" - Reinforces the inclusive approach of the platform, making all users feel welcome.
       - *Call to Action*: Buttons are provided to "Browse Sites" and "Read Journey Insights," ensuring easy navigation to key sections of the website. Each button is clearly labeled with an accompanying icon (e.g., book and read icons), making it visually intuitive.

#### 2. **Main Content Section (`.container`)**
   - **Information Cards (`.card-panel`):**
     - This section uses a three-column grid layout to present key features in a visually balanced and accessible manner. Each column contains a card with a header and a brief description, making the information digestible and easy to scan.

   - **Feature 1: About Us**
     - *Description*: 
       - The "About Us" card introduces the platform, highlighting its role in connecting a community of spiritual travelers. It emphasizes the platform's user-driven nature, where insights and information are shared to aid in planning spiritual journeys.
       - *Context*: 
         - The text mentions the surge in spiritual travel searches in India, framing the platform as a timely and relevant resource for modern spiritual travelers.
- ### Browse Site page
### Detailed Features on the "Browse Sites" Page

#### 1. **Header Section**
   - **Interactive Filter Options:**
     - The "Browse Sites" page begins with a highly interactive filtering system designed to help users easily navigate through the numerous spiritual sites available on the platform.
     - **Filtering by Part of India:**
       - Users can filter the sites based on different geographical regions of India. The filter dropdown allows the selection of specific parts, making it easier for users to explore sites relevant to their travel plans.
     - **Filtering by Deity:**
       - Another dropdown filter lets users narrow down the sites by the deity associated with them. This feature is particularly useful for those looking to visit temples or locations dedicated to a particular deity.
     - **Filter Button:**
       - Once the filters are set, users can apply them using the "Filter" button, which is prominently styled with a black-text-on-orange background, ensuring it's noticeable and easy to use.

   - **Add Site Option (Visible to Logged-In Users Only):**
     - Logged-in users are presented with an option to "Add Site," empowering the community to contribute by adding new spiritual sites to the directory. The button is styled with an orange lighten-2 background, making it visually distinct. It includes an icon (fa-plus) to emphasize its purpose clearly.
     - This feature fosters a collaborative environment, encouraging user-generated content that can benefit others in the community.

   - **Instructional Text:**
     - A small, clear instruction is provided at the top, advising users on how to activate the dropdown filters. This ensures a smooth user experience, particularly for those unfamiliar with the interface.

#### 2. **Body Section**
   - **Collapsible List of Spiritual Sites:**
     - The main body of the page features a collapsible list that dynamically displays the spiritual sites based on the applied filters. The collapsible structure is user-friendly, allowing for a clean and organized presentation of information.
     - **Collapsible Headers:**
       - Each site is introduced with a collapsible header that includes:
         - *Site Name*: Displayed in bold, ensuring that the name of each site stands out.
         - *Icon*: A gopuram icon (fa-gopuram) is used to symbolize temples and spiritual sites, adding a culturally relevant visual cue.
         - *Accessibility Indicator*: If a site is wheelchair accessible, a wheelchair icon is displayed alongside the site name, providing crucial information for users with mobility needs.
       - **Edit and Delete Options (Conditional Display):**
         - If the logged-in user is the creator of a particular site, additional buttons for editing and deleting the site appear within the header. These buttons are styled distinctly (yellow for edit, red for delete) to differentiate their functions, with text-shadow effects to enhance visibility against different backgrounds.
   
   - **Collapsible Body:**
     - When a user clicks on a site's header, the collapsible body expands to reveal detailed information about the site:
       - *Deity*: The specific deity associated with the site is clearly mentioned, aiding users in understanding the religious significance of the location.
       - *Part of India*: This detail situates the site geographically, helping users in their travel planning.
       - *Description*: A comprehensive description of the site is provided, offering users insight into its historical, cultural, and spiritual importance.
- ### Read Insights page
### Detailed Features on the "Read Insights" Page

#### 1. **Header Section**
   - **Page Title:**
     - The "Read Insights" page opens with a clear and centered title, "Journey Insights," setting the stage for users to delve into personal stories, reviews, and insights shared by other spiritual travelers. The title's positioning at the center enhances its visibility and immediately informs users about the page's content.
   
   - **Add Insight Button (Conditional Display):**
     - For logged-in users, the page offers an "Add Insight" button prominently displayed beneath the title. 
     - **Button Styling and Iconography:**
       - The button is styled with an orange lighten-2 background and black text, maintaining a consistent design with other interactive elements across the site. The inclusion of a "fa-plus" icon makes the button's purpose clear at a glance—inviting users to contribute their own travel experiences to the platform.
     - **User Empowerment:**
       - This feature not only encourages user-generated content but also empowers the community to share valuable information and personal experiences, enriching the collective knowledge available on the platform.

#### 2. **Body Section**
   - **Grid Display of Insights:**
     - The main body of the page is designed as a grid layout, effectively organizing multiple user insights into a visually appealing and easily navigable structure. This layout allows for the simultaneous display of numerous insights without overwhelming the user, facilitating easy browsing and comparison of different experiences.
     - **Grid Item Composition:**
       - Each grid item represents an individual user insight and is thoughtfully composed to highlight key aspects of the travel experience:
         - **Location Name:** The name of the location is prominently displayed as the heading of each grid item, immediately informing users about the specific spiritual site or journey being discussed.
         - **Visit Date:** The exact date of the visit is formatted as "dd.mm.yyyy," providing a clear reference to when the experience took place. This is crucial for contextualizing the insight, as experiences may vary depending on the time of year or recent developments at the site.
         - **Rating:** Users can see how the experience was rated, offering a quick indication of the overall satisfaction with the journey.
         - **Purpose of Visit:** This field explains the intent behind the visit, such as pilgrimage, meditation, or cultural exploration, helping others with similar motivations to gauge the relevance of the insight.
         - **Review Description:** A detailed review is provided, where users share their personal experiences, thoughts, and any advice they may have for future visitors. This rich content forms the core value of the page, offering authentic, firsthand accounts of spiritual journeys.
         - **Created By:** The review's author is credited at the bottom of each grid item, fostering a sense of community and accountability. Knowing the author can also help users reach out or connect with others who have similar interests.

   - **Edit and Delete Options (Conditional Display):**
     - If the logged-in user is the creator of a particular review, they are given additional options to edit or delete their insight:
       - **Edit Button:** Allows users to make changes to their original insight, ensuring that information remains accurate and up-to-date. The button is styled in yellow accent-3 with black text, making it distinct but complementary to the overall design.
       - **Delete Button:** Users can also choose to delete their insight if it is no longer relevant or if they wish to remove it for any other reason. The delete button is styled with a red darken-4 background and black text, with a subtle text-shadow effect for emphasis. This styling alerts users to the button's significance, reducing accidental deletions.
     - **Conditional Logic:** The edit and delete buttons are only visible to the author of the insight, ensuring that users have control over their contributions while preventing unauthorized changes.
- ### Edit Sites page
### Detailed Features on the "Edit Site" Page

#### 1. **Header Section**
   - **Page Banner:**
     - The header section opens with a banner that communicates the page’s purpose: allowing users to update and refine existing site entries.
     - **Message Content:**
       - The banner text, “Want to Edit a Site Entry? We're always want to keep our community's knowledge and experiences up-to-date,” is designed to encourage users to contribute to the platform's accuracy and relevance. It highlights the importance of maintaining up-to-date information, fostering a collaborative spirit.
     - **Text Styling:**
       - The text is centrally aligned, with the primary call to action ("Want to Edit a Site Entry?") underlined for emphasis, drawing attention to the page's functionality.

#### 2. **Body Section**
   - **Form Structure:**
     - The main body contains a well-organized form that allows users to update information about a specific spiritual site. The form is centrally placed and neatly presented within a card panel, ensuring a clean, user-friendly experience.

   - **Input Fields:**
     - **Site Name Input Field:**
       - **Icon and Field:** The site name is prefixed by a "fa-gopuram" icon, visually associating the field with the cultural or spiritual significance of the site. The field enforces a text pattern validation and limits input to between 2 and 100 characters, ensuring that names are correctly formatted and of appropriate length.
       - **Pre-filled Value:** The input field is pre-filled with the existing site name, making it easy for users to identify and edit as needed.
       - **Label Styling:** The label for the site name is styled in black text, maintaining a consistent theme, and is set as active to indicate that the field is pre-populated.

     - **Deity Field:**
       - **Icon and Field:** The deity associated with the site is represented by a "fa-hands-praying" icon. The input field requires text input with a pattern allowing between 2 and 20 characters, reflecting the deity's name. This field is marked as required, emphasizing its importance in describing the site.
       - **Validation:** The validation ensures that users input a proper name, avoiding any formatting errors.
       - **Pre-filled Value:** The field is pre-filled with the current deity name, simplifying the editing process.

     - **Part of India Location Selection:**
       - **Icon and Dropdown:** The dropdown is prefixed with a "fa-compass" icon, symbolizing direction or location. Users can select the part of India where the site is located from a predefined list.
       - **Dynamic Selection:** The dropdown automatically highlights the part of India currently associated with the site, thanks to the conditional selection logic, making the editing process straightforward.
       - **Label:** The label is actively displayed, and the field is required to ensure this essential information is captured.

     - **Description Field:**
       - **Icon and Textarea:** The description field, preceded by a "fa-rectangle-list" icon, allows users to provide detailed information about the site. The textarea enforces a character count between 5 and 800, giving enough room for detailed descriptions while preventing overly lengthy entries.
       - **Pre-filled Text:** The textarea is pre-filled with the site's existing description, making it easy for users to revise or update the content.
       - **Label:** The label remains active and styled in black text, ensuring clarity in what the field is asking for.

     - **Disabled Access Checkbox:**
       - **Checkbox and Icon:** The disabled access feature is represented by a checkbox with an adjacent "fa-wheelchair" icon, making the feature easily recognizable. The checkbox is pre-checked if the site currently has disabled access, reflecting the existing data.
       - **Label and Tooltip:** The label encourages inclusivity by highlighting the importance of noting whether the site is accessible to those with disabilities.

   - **Submit Button:**
     - **Button Placement and Styling:**
       - The submit button is centrally placed within the form, with the text "Update" indicating the action's purpose. The button is styled with an orange background and black text, consistent with the site's design palette, ensuring it stands out as the primary call to action on the page.
       - **Iconography:** Although no additional icon is present with the button text, the straightforward design and color contrast make the button highly visible and inviting.
- ### Edit Insights page
### Detailed Features on the "Edit Insights" Page

#### 1. **Header Section**
   - **Page Banner:**
     - The header section features a prominent banner that outlines the purpose of the page: enabling users to edit their previously shared journey insights.
     - **Message Content:**
       - The banner text reads, “Want to Edit a Journey Insight? We're always want to keep our community's knowledge and experiences up-to-date,” which serves as a prompt for users to refine and update their insights, reinforcing the collaborative nature of the platform.
     - **Text Styling:**
       - The primary call to action, “Want to Edit a Journey Insight?” is underlined for emphasis, ensuring it grabs the user’s attention. The text is center-aligned, making it easily readable and visually appealing.

#### 2. **Body Section**
   - **Form Structure:**
     - The main body contains a structured form that allows users to update their journey insights. This form is centrally located within a card panel, providing a clean and organized layout that is easy to navigate.

   - **Input Fields:**
     - **Where Did You Go Field:**
       - **Icon and Field:** This field is designed to capture the name of the location visited, prefixed with a "fa-gopuram" icon to symbolically represent the nature of the journey. The field accepts text input with a validation pattern, requiring the input to be between 2 and 100 characters, ensuring the entry is concise yet descriptive.
       - **Pre-filled Value:** The field is pre-filled with the existing location name, making it simple for users to make adjustments if necessary.
       - **Label Styling:** The label for this field is set to active with black text, maintaining consistency with the page's overall design.

     - **Rating Field:**
       - **Icon and Field:** This field is dedicated to capturing the user’s rating of their experience, represented by a "fa-hands-praying" icon. The field requires text input, ensuring that the rating is formatted correctly within a 2 to 20 character limit.
       - **Pre-filled Value:** The field is pre-filled with the current rating, allowing users to easily update their experience rating.
       - **Label Styling:** The label is active, providing clarity on what information the field is requesting.

     - **When Did You Go Field:**
       - **Icon and Datepicker:** The visit date field is marked with a "fa-calendar-alt" icon, linking it to the idea of time or scheduling. It includes a date picker for ease of use, allowing users to select the date they visited the site. This date is formatted as "dd.mm.yyyy" and is pre-filled based on the existing data.
       - **Label:** The label is actively displayed above the date picker, ensuring users understand the field's purpose.

     - **Purpose Field:**
       - **Icon and Field:** The purpose of the visit is captured in this field, marked with a "fa-rectangle-list" icon, symbolizing a list or explanation. This text input requires the purpose to be concise, falling between 2 and 20 characters.
       - **Pre-filled Value:** The field comes pre-filled with the user's previously stated purpose, streamlining the editing process.
       - **Label:** The label remains active, clearly communicating the field’s intent.

     - **Description Field:**
       - **Textarea and Label:** This textarea is where users can elaborate on their experience. The field is styled to be center-aligned with a clear, prominent label reading, “Tell Us More About Your Experience!” This encourages detailed and thoughtful input, with the field requiring between 5 and 800 characters.
       - **Pre-filled Text:** The textarea is pre-filled with the existing review description, allowing for easy updates and revisions.
       - **Label Styling:** The label is styled in black text to remain consistent with the other fields, ensuring the page maintains a cohesive look.

   - **Submit Button:**
     - **Button Placement and Styling:**
       - The submit button is prominently placed at the bottom of the form, with the text "Update" clearly indicating its function. The button is styled with an orange background and black text, matching the site’s design scheme. This ensures the button stands out as the primary call to action on the page.
       - **Iconography:** The button does not include an additional icon, but the color contrast and central placement make it immediately noticeable and easy to interact with.
- ### Register page
### Detailed Features on the "Register" Page

The "Register" page is designed to provide a seamless and user-friendly experience for new users to create an account on the platform. Below is a breakdown of the key features and elements of the page:

#### 1. **Header Section**
   - **Page Banner:**
     - The banner at the top of the page serves as a prompt for users who might already have an account.
     - **Text Content:**
       - The banner text reads, “Already Have a Profile?” followed by a link, “Sign In Here!” which directs users to the login page if they are existing members.
     - **Link Styling:**
       - The "Sign In Here!" link is styled with a light-blue text color (`text-darken-4`), making it stand out against the rest of the banner text. This provides a clear call-to-action for existing users while maintaining the page's overall aesthetic.

#### 2. **Body Section**
   - **Form Layout:**
     - The registration form is centrally located within a card panel, ensuring that it is the focal point of the page. The form uses a simple and clean layout that guides the user through the registration process step-by-step.

   - **Input Fields:**
     - **Username Field:**
       - **Icon and Field:** The username field is accompanied by a "fa-user-plus" icon, which visually represents user creation. The input field is set up to accept an alphanumeric username between 5 and 8 characters in length.
       - **Validation and Requirements:** The input field has validation rules enforcing the character length and type, ensuring that the username meets the platform’s criteria.
       - **Label and Helper Text:** The label, “Username,” is styled in black text and is accompanied by helper text that clearly explains the required format: “An alphanumeric value of 5-8 characters.”

     - **Password Field:**
       - **Icon and Field:** The password field is identified with a "fa-lock" icon, indicating security. Users are required to create a password with similar constraints to the username: an alphanumeric string between 5 and 8 characters.
       - **Validation:** The password field includes validation to ensure that the input meets the required format.
       - **Label and Helper Text:** The label, “Password,” is also in black text, with helper text explaining the requirements, “An alphanumeric value of 5-8 characters.”

     - **Confirm Password Field:**
       - **Icon and Field:** This field is similar in appearance to the password field, also using the "fa-lock" icon, but its purpose is to confirm the user's password. It ensures that users correctly enter their intended password by requiring them to input it twice.
       - **Validation:** The field includes validation to check that the confirm password matches the initial password input, reducing errors during registration.
       - **Label and Helper Text:** The label is clear, and the helper text reminds users to “Ensure this matches the password above.”

   - **Register Button:**
     - **Button Styling and Placement:**
       - The "Register" button is styled prominently with a large, full-width design in black with white text. This ensures it is the most noticeable element on the page and is placed at the bottom of the form to conclude the registration process.
       - **Iconography:** The button includes a "fa-sign-in-alt" icon, reinforcing the idea of signing up or registering for the platform.
       - **Action:** Clicking the button submits the form data for processing, initiating the registration of a new user account.
------------            
- ### Traceability Matrix
    ![Table][def74]
------------
- ## **Logic**
    * The initial flowchart designed to the basic quiz interactivity is as follows:
    ![Flowchart] [def25]
------------    
- ## **Technologies Used**
------------
+ ### Languages Used
    * #### HTML5
    * #### CSS3
    * #### Javascript
+ ### Frameworks, Libraries and Programs Used
    * #### [Cdnfonts][Cdnfonts] : was used to import Samarkan fonts into style.css file which has been used in the Main Logo title.
    * #### [Font Awesome][def9] : was used to add icons for aesthetic and UX purposes. Icons have been used to for guide and music toggle button which can be easily identified by users regarless of their English language level. Icon has also been used for prefix to questions to make the quiz look more playfull.
    * #### [Git][def10]: was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
    * #### [GitHub][def11] : It is used as the repository for the project's code after being pushed from Git.
    * #### [Powerpoint][def12] : was used for resizing images and editing photos and screenshots for Readme. It is also used for designing flyers for event pages.
    * #### [Balsamiq][def13] : was used to create the wireframes during the design process.
    * #### [Coolors][def14] : was used to find complimenting colors to the backgorund image for the website color palette.
    * #### [TinyPng][def15] : was used to compress the images that are used in the website, especially on the gallery page.     
    * #### [Bootstrap][def17] : codes from Bootsrap grid html and Css library has been used to design the Question and answers section to have a responsive quiz layout in columns and rows.
    * #### [Autoprefixer CSS online][def18] : has been used to parse the CSS in style.css to add different browser prefixes to ensure the CSS works on all browsers.
    * #### [favicon.io][def19] : was used to generate the favicon for the website.
    * #### [W3C Markup Validation Service][def20] : has been used to validate the code on all pages and style.css.
    * #### [UI.Dev][def22] : was used to generate Mockup Screenshots.
    * #### [Free Formatter][def23] : was used to ensure proper indentation in the HTML and CSS codes.
    
- ## **Testing**
------------
+ ### Validator Testing Results
    * Javascript was tested using JSHint
    JSHint highlighted some undefined variables and unused functions. These were due to them being used/accessed from within the HTML pages rather than within the script itself.

    * Css was validated using https://jigsaw.w3.org/css-validator/#validate_by_input+with_options
    No issues found
    
+ ### Lighthouse Testing
    

+ ### Responsiveness Testing Results
    ![Results][def26]
    ![Results][def27]
    ![Results][def28]
    ![Results][def30]
    ![Results][def31]
    ![Results][def32]

            
- ## Bugs and Fixes
------------
* 

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
    * Most of the question and answers are adapted from jagranJosh website [JagranJosh][def75]
    * All other content has been drafted by the developer.

- ### Code
    * Code on how to present a modal and close was created with the help of a tutorial on [WebDevSimplified][def76].
    * Code for the hover effect on info cards on Home page was an play around with some examples from  [Codepen]
    * I have used Bootstrap grid classes to implement structure for the quiz.
    * The basic logic for the quiz has been based on a tutorial by Avinash Kr from ![GreatStack][def21]
    * Hover effects on throughout has been created by using tutorials on [W3schools](https://www.w3schools.com/cssref/sel_hover.php)

- ### Media
    * ![Favicon][def1] a vector art by ([Scigola](https://pixabay.com/vectors/symbol-om-religion-1537054/))
    * ![Background Image][def0]   

- ## Gratitude
    * I would like to thank my mentor Dick Vlaanderen for all the coaching and helping me with their insight and experience.
    * Thanks to tutor Roo, who helped me fix my deployment.
    * Thank you to Md—Fahim Kabir Hamim for the lessons on Tech2 etc.
    * Thanks to tutors from Great Stck.
    * Thanks to Amy our facilitator for running our regular Stand-ups which gave me confidence.






[Cdnfonts]: https://www.cdnfonts.com/samarkan.font
[def0]: ./documentation/backgroundimage.png
[def1]: ./documentation/favicon.png
[def2]: #c-frequent-user-goals
[def3]: #future-implementations
[def4]: ./documentation/wireframe1.png
[def5]: ./documentation/wireframe2.png
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
[def17]: https://getbootstrap.com/
[def18]: https://autoprefixer.github.io/
[def19]: https://favicon.io/
[def20]: https://validator.w3.org/
[def21]: https://linktr.ee/iamavinashkr
[def22]: https://ui.dev/amiresponsive?url=https://ashwinsel.github.io/Milestone-1/index.html
[def23]: https://www.freeformatter.com/html-formatter.html
[def24]: ./documentation/home-ss.png
[def25]: ./documentation/flowchart1.png
[def26]: ./documentation/home-ss.png
[def27]: ./documentation/ss-browsesites.png
[def28]: ./documentation/ss-addinsight.png
[def29]: ./documentation/colour-pallete.png
[def30]: ./documentation/ss-register.png
[def31]: ./documentation/ss-signin.png
[def32]: ./documentation/ss-readinsight.png
[def33]: ./documentation/ipadair.png
[def34]: ./documentation/1024px.png
[def35]: ./documentation/ipadpro.png
[def36]: ./documentation/desktopmore1200px.jpg
[def42]: https://yatra1-4cc0076860db.herokuapp.com/
[def43]: ./documentation/samarkanfont.png
[def44]: ./documentation/spacemonofont.png
[def45]: ./documentation/lugrasimofont.png
[def46]: ./documentation/main-img.png
[def47]: ./documentation/musiconoff.png
[def49]: ./static/img/chakra.png
[def50]: ./documentation/reset.png
[def64]: ./documentation/rightans.png
[def65]: ./documentation/wrongans.png
[def66]: ./documentation/nextbutton.png
[def67]: ./documentation/scorebox.png
[def68]: ./documentation/guidemodal.png
[def69]: https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Fashwinsel.github.io%2FMilestone-1%2F#textarea
[def70]: https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Fashwinsel.github.io%2FMilestone-1%2F#textarea
[def74]: ./documentation/traceability-matrix.png
[def75]: https://www.jagranjosh.com/general-knowledge/gk-quiz-on-hindu-mythology-1706194424-1
[def76]: https://courses.webdevsimplified.com/
[def78]: ./documentation/menubar.png