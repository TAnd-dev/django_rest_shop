import React from 'react'
import { Link } from 'react-router-dom'
import './Header.scss'

function HeaderDesktop() {
	return (
		<div id='header--desktop' className='header--desktop'>
			<div className='header-top'>
				<div className='header-top__container'>
					<div className='header-top__menu'>
						<ul className='header-top__menu-list'>
							{/* Select City */}
							<li className='header-top__menu-item'>
								<Link to=''>
									<div className='header-top__menu-link'>
										<div className='city-select'>
											<svg
												className='icon-location'
												width={12}
												height={12}
												viewBox='0 0 12 12'
												xmlns='http://www.w3.org/2000/svg'
											>
												<path d='M6 11L5.62895 11.3351L6 11.7459L6.37105 11.3351L6 11ZM6 0.5C3.78886 0.5 2 2.28886 2 4.5H3C3 2.84114 4.34114 1.5 6 1.5V0.5ZM10 4.5C10 2.28886 8.21114 0.5 6 0.5V1.5C7.65886 1.5 9 2.84114 9 4.5H10ZM6 11C6.37105 11.3351 6.37112 11.3351 6.3712 11.335C6.37125 11.3349 6.37134 11.3348 6.37143 11.3347C6.37161 11.3345 6.37185 11.3343 6.37213 11.3339C6.3727 11.3333 6.37349 11.3324 6.37448 11.3313C6.37646 11.3291 6.37928 11.326 6.3829 11.3219C6.39013 11.3138 6.40059 11.3021 6.41405 11.2868C6.44097 11.2564 6.47993 11.2119 6.52919 11.1547C6.6277 11.0404 6.7676 10.875 6.9351 10.6686C7.26967 10.2564 7.71658 9.67788 8.16448 9.01403C8.61142 8.3516 9.06553 7.59509 9.40943 6.82747C9.75039 6.0664 10 5.25742 10 4.5H9C9 5.05508 8.81211 5.71485 8.49682 6.41862C8.18447 7.11584 7.76358 7.82028 7.33552 8.45472C6.90842 9.08775 6.48033 9.64207 6.15865 10.0384C5.99803 10.2363 5.86448 10.3942 5.77159 10.502C5.72515 10.5559 5.68891 10.5973 5.66456 10.6248C5.65239 10.6386 5.64319 10.6489 5.63718 10.6557C5.63418 10.659 5.63197 10.6615 5.63059 10.663C5.6299 10.6638 5.62942 10.6643 5.62914 10.6646C5.629 10.6648 5.62892 10.6649 5.62889 10.6649C5.62887 10.6649 5.62889 10.6649 5.62888 10.6649C5.62891 10.6649 5.62895 10.6649 6 11ZM2 4.5C2 5.25742 2.24961 6.0664 2.59057 6.82747C2.93447 7.59509 3.38858 8.3516 3.83552 9.01403C4.28342 9.67788 4.73033 10.2564 5.0649 10.6686C5.2324 10.875 5.3723 11.0404 5.4708 11.1547C5.52007 11.2119 5.55903 11.2564 5.58595 11.2868C5.59941 11.3021 5.60987 11.3138 5.6171 11.3219C5.62072 11.326 5.62354 11.3291 5.62552 11.3313C5.62651 11.3324 5.6273 11.3333 5.62787 11.3339C5.62815 11.3343 5.62839 11.3345 5.62857 11.3347C5.62866 11.3348 5.62875 11.3349 5.6288 11.335C5.62888 11.3351 5.62895 11.3351 6 11C6.37105 10.6649 6.37109 10.6649 6.37112 10.6649C6.37111 10.6649 6.37113 10.6649 6.37111 10.6649C6.37108 10.6649 6.371 10.6648 6.37086 10.6646C6.37058 10.6643 6.3701 10.6638 6.36941 10.663C6.36803 10.6615 6.36582 10.659 6.36282 10.6557C6.35681 10.6489 6.34761 10.6386 6.33544 10.6248C6.31109 10.5973 6.27485 10.5559 6.22841 10.502C6.13552 10.3942 6.00197 10.2363 5.84135 10.0384C5.51967 9.64207 5.09158 9.08775 4.66448 8.45472C4.23642 7.82028 3.81553 7.11584 3.50318 6.41862C3.18789 5.71485 3 5.05508 3 4.5H2ZM6 5.25C5.58614 5.25 5.25 4.91386 5.25 4.5H4.25C4.25 5.46614 5.03386 6.25 6 6.25V5.25ZM6.75 4.5C6.75 4.91386 6.41386 5.25 6 5.25V6.25C6.96614 6.25 7.75 5.46614 7.75 4.5H6.75ZM6 3.75C6.41386 3.75 6.75 4.08614 6.75 4.5H7.75C7.75 3.53386 6.96614 2.75 6 2.75V3.75ZM5.25 4.5C5.25 4.08614 5.58614 3.75 6 3.75V2.75C5.03386 2.75 4.25 3.53386 4.25 4.5H5.25Z'></path>
											</svg>

											<span className='city-select__text'>
												Петропавловск-Камчатский
											</span>
										</div>
									</div>
								</Link>
							</li>
							{/* Header Menu */}
							<li className='header-top__menu-item'>
								<Link to='/'>Акции</Link>
							</li>
							<li className='header-top__menu-item'>
								<Link to='/'>Магазины</Link>
							</li>
							<li className='header-top__menu-item header-top-menu-item__dropdown menu-dropdown'>
								<Link to='/'>Покупателям</Link>
							</li>
							<li className='header-top__menu-item'>
								<Link to='/'>Юридическим лицам</Link>
							</li>
							<li className='header-top__menu-item'>
								<Link to='/'>Клуб DNS</Link>
							</li>
						</ul>
					</div>
					{/* Block for number */}
					<ul className='header-top__profile-list'>
						<li className='profile-list__tel'>
							<Link className='' to='tel:8-800-77-07-999'>
								8-800-77-07-999
							</Link>
							<span className='profile-list__text'>(c 12:00 до 07:00)</span>
						</li>
					</ul>
				</div>
			</div>
		</div>
	)
}

export default HeaderDesktop
